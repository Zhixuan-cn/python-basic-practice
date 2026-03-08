# reverse print 10 charactors
def reverse_print(chars):
    if len(chars) == 0:
        return
    print(chars[-1], end='')  
    reverse_print(chars[:-1])

if __name__ == "__main__":
    while True:
        cha = input("input 10 charactors：")
        if len(cha) == 10:
            break
        print(f"error！you input {len(cha)} charactors，make sure input 10 charactors.")
    
print("output:", end='')
reverse_print(cha)



