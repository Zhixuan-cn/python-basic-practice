if __name__ == '__main__':
    import time
    import random

    # Would you like to start the game
    play_it = input('Do you want to play it? (\'y\' or \'n\'): ').strip().lower()
    
    while play_it == 'y':
        c = input('Input a character (optional):\n').strip()
        
        # random generate number
        target_num = random.randint(0, 99) 
        print('Please guess a number between 0 and 99:\n')
        
        # record start time
        start_time = time.perf_counter()  
        a = time.time()  
        
        # first number guess
        while True:
            try:
                guess = int(input('Input your guess: ').strip())
                if 0 <= guess <= 99:
                    break
                else:
                    print('Error! Please input an integer between 0 and 99!')
            except ValueError:
                print('Error! Please input an integer (0-99)!')
        
        # guess looping
        while guess != target_num:
            if guess > target_num:
                print('Too high! Please guess a smaller number!')
            else:
                print('Too low! Please guess a bigger number!')
            
            # guess again
            while True:
                try:
                    guess = int(input('Input your guess: ').strip())
                    if 0 <= guess <= 99:
                        break
                    else:
                        print('Error! Please input an integer between 0 and 99!')
                except ValueError:
                    print('Error! Please input an integer (0-99)!')
        
        # Calculte time and score
        end_time = time.perf_counter()
        b = time.time()
        

        time_used = end_time - start_time
        # Base score of 100 minus (time elapsed × 5) (95 points for 1 second, 0 points for 20 seconds)
        score = max(0, 100 - time_used * 5)
        print(f"Your score (higher is better): {score:.1f}") 
        
        # print time
        total_time = b - a
        print(f"It took you {total_time:.3f} seconds")
        
        # score prompts
        if score >= 80:
            print('You are very clever! 🎉')
        elif score >= 50:
            print('You did a good job! 😊')
        else:
            print('Keep trying! 💪')
        
        # game success prompts
        print('Congratulations! You guessed the right number!')
        print(f"The number is: {target_num}")  

        # ask if you want to continue game
        play_it = input('\nDo you want to play again? (\'y\' or \'n\'): ').strip().lower()
    
    # game over
    print('Game over! Thanks for playing. 👋')