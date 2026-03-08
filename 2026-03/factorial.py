# Find the sum of 1 + 2! + 3! + … + 20!
sum = 0  
factorial = 1 

for i in range(1, 21):
    factorial *= i  
    sum += factorial  

print(f"sum of 1+2!+3!+...+20!：{sum}")


