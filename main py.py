main py

import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")
    
    secret_number = random.randint(1, 50)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You found the number in {attempts} attempts!")
                
                play_again = input("Would you like to play again? (yes/no): ")
                if play_again.lower() == "yes":
                    play_game()
                else:
                    print("Thanks for playing! See you next time.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    play_game()
    