# Fraction sequence: 2/1, 3/2, 5/3, 8/5, 13/8, 21/13..., find the sum of the first 20 terms of the sequence.
sum = 0.0  
numerator = 2    
denominator = 1 
count = 20       

for i in range(count):
    sum += numerator / denominator
    temp = numerator
    numerator = numerator + denominator  # 新分子 = 原分子 + 原分母
    denominator = temp                   # 新分母 = 原分子

print(f"Sum of {count}：{sum:.4f}")
