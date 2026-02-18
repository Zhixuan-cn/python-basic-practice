def print_chessboard_with_stars():
    print("\n=== chessboard ===")
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

if __name__ == "__main__":
    print_chessboard_with_stars()
