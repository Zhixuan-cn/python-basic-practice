# Judge whether a five-digit number is a palindrome number
while True:
    try:
        num = int(input("Enter a 5-digit number："))
        if 10000 <= num <= 99999:
            break
        else:
            print("Input error! Enter a 5-digit number between 10000 and 99999.")
    except ValueError:
        print("Input error! Enter a valid integer.")

wan = num // 10000          
qian = (num // 1000) % 10   
shi = (num // 10) % 10      
ge = num % 10               

if wan == ge and qian == shi:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
