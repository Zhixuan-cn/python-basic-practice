import pygame
import random
import math

# 初始化pygame
pygame.init()

# 设置屏幕尺寸（兼容非全屏模式，避免分辨率异常）
try:
    screen_info = pygame.display.Info()
    WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h
    # 防止全屏权限问题，改用窗口模式（也可改回FULLSCREEN）
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
except:
    # 备用分辨率，避免获取屏幕信息失败
    WIDTH, HEIGHT = 1280, 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("壮美烟花特效")

# 颜色定义（烟花主色+渐变，确保都是合法RGB值）
COLORS = [
    (255, 0, 0),    # 红
    (255, 165, 0),  # 橙
    (255, 255, 0),  # 黄
    (0, 255, 0),    # 绿
    (0, 0, 255),    # 蓝
    (128, 0, 128),  # 紫
    (255, 192, 203),# 粉
    (255, 255, 255) # 白
]

# 时钟（控制帧率）
clock = pygame.time.Clock()

# 粒子类（烟花粒子）- 彻底修复颜色和尺寸问题
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        # 随机粒子速度（角度+大小）
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1, 6)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        
        # 修复1：严格限制颜色值在0-255之间（同时限制上下限）
        r = max(0, min(color[0] + random.randint(-20, 20), 255))
        g = max(0, min(color[1] + random.randint(-20, 20), 255))
        b = max(0, min(color[2] + random.randint(-20, 20), 255))
        self.color = (r, g, b)  # 确保是合法的RGB三元组
        
        # 粒子大小和生命周期（初始尺寸≥1，避免0）
        self.size = random.uniform(2, 4)
        self.life = random.randint(60, 120)  # 粒子存活帧数
        self.gravity = 0.05  # 重力影响

    def update(self):
        # 更新位置（加入重力）
        self.vy += self.gravity
        self.x += self.vx
        self.y += self.vy
        # 粒子减速
        self.vx *= 0.98
        self.vy *= 0.98
        # 生命周期减少
        self.life -= 1
        # 修复2：粒子尺寸最小为1，避免0
        self.size = max(1, self.size - 0.02)

    def draw(self):
        # 修复3：透明度通过Surface设置，颜色仅用RGB
        alpha = int(255 * (self.life / 120))  # 生命周期越短越透明
        # 确保alpha在0-255之间
        alpha = max(0, min(alpha, 255))
        
        # 创建带透明通道的Surface
        s_size = int(self.size * 2)
        s = pygame.Surface((s_size, s_size), pygame.SRCALPHA)
        # 设置Surface透明度
        s.set_alpha(alpha)
        
        # 绘制圆形（尺寸和颜色均合法）
        center = (int(self.size), int(self.size))
        radius = int(self.size)
        pygame.draw.circle(s, self.color, center, radius)
        
        # 绘制到主屏幕（位置取整，避免浮点误差）
        screen.blit(s, (int(self.x - self.size), int(self.y - self.size)))

# 烟花类（发射轨迹+爆炸）
class Firework:
    def __init__(self):
        # 随机发射起点（屏幕底部，避免越界）
        self.x = random.randint(WIDTH//4, WIDTH*3//4)
        self.y = HEIGHT
        # 随机爆炸高度（屏幕中上部更美观）
        self.target_y = random.randint(HEIGHT//4, HEIGHT//2)
        # 发射速度
        self.speed = random.uniform(8, 15)
        # 烟花主色（直接取合法颜色）
        self.color = random.choice(COLORS)
        # 是否爆炸
        self.exploded = False
        # 爆炸后的粒子列表
        self.particles = []

    def update(self):
        if not self.exploded:
            # 向上发射（限制位置，避免越界）
            self.y -= self.speed
            self.x = max(0, min(self.x + random.uniform(-0.5, 0.5), WIDTH))
            # 到达目标高度则爆炸
            if self.y <= self.target_y:
                self.explode()
                self.exploded = True
            # 绘制发射轨迹（用合法颜色）
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 3)
        else:
            # 更新爆炸后的粒子（过滤已死亡的粒子）
            new_particles = []
            for p in self.particles:
                p.update()
                if p.life > 0:
                    new_particles.append(p)
                    p.draw()
            self.particles = new_particles

    def explode(self):
        # 生成爆炸粒子（数量适中，避免性能问题）
        particle_count = random.randint(150, 250)
        for _ in range(particle_count):
            self.particles.append(Particle(self.x, self.y, self.color))

# 主循环
def main():
    fireworks = []
    running = True
    # 背景色（黑色更凸显烟花）
    bg_color = (0, 0, 0)
    
    while running:
        # 控制帧率（60帧流畅）
        clock.tick(60)
        
        # 事件处理（按ESC/关闭窗口退出）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # 填充背景（半透明叠加，保留轨迹残影）
        screen.fill(bg_color, special_flags=pygame.BLEND_RGBA_MULT)
        
        # 随机生成新烟花（控制频率，避免太密集）
        if random.random() < 0.05:
            fireworks.append(Firework())
        
        # 更新并绘制所有烟花（过滤已结束的烟花）
        new_fireworks = []
        for fw in fireworks:
            fw.update()
            if not fw.exploded or len(fw.particles) > 0:
                new_fireworks.append(fw)
        fireworks = new_fireworks
        
        # 更新屏幕
        pygame.display.flip()
    
    # 安全退出pygame
    pygame.quit()

if __name__ == "__main__":
    main()