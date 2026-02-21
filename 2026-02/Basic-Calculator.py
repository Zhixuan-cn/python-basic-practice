import os  
try:
    from art import logo
except ImportError:
    logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
    """

def clear_screen():
    try:
        from replit import clear
        clear()
    except ImportError:
        os.system('cls' if os.name == 'nt' else 'clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print(" Error: Cannot divide by zero!")
        return None
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    clear_screen()  
    print(logo)
    
    while True:
        num1_input = input("What is the first number?\n").strip()
        try:
            num1 = float(num1_input)
            break
        except ValueError:
            print(" Invalid input! Please enter a valid number.")
    
    print("\nAvailable operations:")
    for symbol in operations:
        print(f"  {symbol}")
    
    repeat = True
    while repeat:
        while True:
            operation_symbol = input("\nPick an operation:\n").strip()
            if operation_symbol in operations:
                break
            print(f"Invalid operation! Please choose from: {list(operations.keys())}")
        
        while True:
            num2_input = input("What is the next number?\n").strip()
            try:
                num2 = float(num2_input)
                break
            except ValueError:
                print("Invalid input! Please enter a valid number")
        
        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)
        
        if answer is None:
            continue
        
     
        print(f"\n {num1} {operation_symbol} {num2} = {answer}")
        
        while True:
            continue_choice = input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or 'q' to quit.\n").lower().strip()
            if continue_choice in ["y", "n", "q"]:
                break
            print(" Invalid input! Please type 'y', 'n', or 'q'.")
        
        if continue_choice == "y":
            num1 = answer  
        elif continue_choice == "n":
            repeat = False
            calculator() 
        elif continue_choice == "q":
            repeat = False
            clear_screen()
            print("Goodbye.")

calculator()
