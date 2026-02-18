def oct_to_dec_builtin():
    """
     octal to decimal conversion
    """
    # input verification
    while True:
        oct_input = input("input octal number：").strip()
        # remove prefix '0o'
        oct_str = oct_input.lstrip('0o') if oct_input.startswith(('0o', '0O')) else oct_input
        
        if not oct_str:
            print("Error! Input cannot be empty")
            continue
        
        try:
            # int(string, 8) verify whether the number is octal or not
            dec_num = int(oct_str, 8)
            break
        except ValueError:
            print("Error Input is not a valid octal number, please re-enter (digits 0-7 only).")
    
    # output
    print(f"\noctal {oct_input} convert decimal：{dec_num}")

if __name__ == "__main__":
    oct_to_dec_builtin()
