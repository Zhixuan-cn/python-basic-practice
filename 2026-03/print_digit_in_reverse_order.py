#   process a positive integer with no more than 6 digits, output the number of digits, and print each digit in reverse order.
def process_number():
    while True:
        user_input = input("Please enter a positive integer with no more than 6 digits：")      
        if not user_input.isdigit():
            print("Input error! Need enter a positive integer; negative numbers, decimals, or letters are not allowed.")
        elif len(user_input) > 6:
            print(f"Input error! The number you entered has {len(user_input)} digits, and a maximum of 6 digits is allowed.")
        elif user_input == "0":
            print("Input error! 0 is not a positive integer; please re-enter a valid number.")
        else:
            break 
    num_str = user_input
    digit_count = len(num_str)
    print(f"\n The number you entered has {digit_count} digits.")
    reversed_num_str = num_str[::-1] 
    print("Reversed digits:", end=" ")
    for digit in reversed_num_str:
        print(digit, end=" ")
if __name__ == "__main__":
    process_number()
p