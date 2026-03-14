#   Determine the day of the week.
def get_weekday():
    week_rules = {
        'm': 'Monday',
        'tu': 'Tuesday',
        'th': 'Thursday',
        'w': 'Wednesday',
        'f': 'Friday',
        'sa': 'Saturday',
        'su': 'Sunday'
    }
    while True:
        first_char = input("Please enter the first letter of the weekday（M/T/W/F/S）：").strip().lower()
        if first_char in ['m', 't', 'w', 'f', 's']:
            break
        print("Invalid input! The first letter can only be M/T/W/F/S; please re-enter it.")
    if first_char in ['m', 'w', 'f']:
        weekday = week_rules[first_char]
    elif first_char == 't':
        while True:
            second_char = input("The first letter is T; please enter the second letter (u/h):").strip().lower()
            if second_char in ['u', 'h']:
                key = first_char + second_char
                weekday = week_rules[key]
                break
            print("Invalid input! The second letter can only be u (Tuesday) or h (Thursday); please re-enter it.")
    else:  # first_char == 's'
        while True:
            second_char = input("First letter is S; please enter the second letter (a/u):").strip().lower()
            if second_char in ['a', 'u']:
                key = first_char + second_char
                weekday = week_rules[key]
                break
            print("Invalid input! The second letter can only be a (Saturday) or u (Sunday). Please re-enter.")
    print(f"\n Your input letters correspond to: {weekday} ({weekday [:3]})")
if __name__ == "__main__":
    print("=== Determine the day of the week ===")
    print("Supported initial letters are M/T/W/F/S; some require entering a second letter.\n")
    get_weekday()
