 # Sort ten numbers
def sort_numbers():
    numbers = []
    print("Enter 10 numbers：")
    for i in range(10):
        while True:
            try:
                num = float(input(f"Enter the (i+1) number："))
                numbers.append(num)
                break
            except ValueError:
                print("Input error! Please enter a valid number.")
    
    sorted_asc = sorted(numbers)  
    sorted_desc = sorted(numbers, reverse=True)  
    
    print("\n===== Sorting result =====")
    print(f"Original data：{numbers}")
    print(f"ascending order：{sorted_asc}")
    print(f"descending order：{sorted_desc}")

if __name__ == "__main__":
    sort_numbers()
