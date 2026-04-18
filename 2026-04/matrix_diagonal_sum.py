 # Sum of the diagonal elements of a matrix
def matrix_diagonal_sum():
    matrix = []
    print("Enter elements of a matrix：")
    for i in range(3):
        while True:
            try:
                row_input = input(f"Input {i+1} line：").strip()
                row = [float(num) for num in row_input.split()]
                if len(row) != 3:
                    print(f"Input error! Please enter three numbers")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("input error, enter valid number")
    
    main_sum = 0  
    sub_sum = 0   
    for i in range(3):
        for j in range(3):
            if i == j:
                main_sum += matrix[i][j]
            if i + j == 2:
                sub_sum += matrix[i][j]
    
    print("The input 3×3 matrix：")
    for row in matrix:
        print(f"[{row[0]:^5.1f}, {row[1]:^5.1f}, {row[2]:^5.1f}]")
    print(f"\nSum of the main diagonal：{main_sum:.1f}")
    print(f"Sum of the sub-diagona：{sub_sum:.1f}")
 
if __name__ == "__main__":
    matrix_diagonal_sum()

