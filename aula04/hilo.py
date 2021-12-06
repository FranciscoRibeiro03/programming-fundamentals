# Complete the code to make the HiLo game...

import random

def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101);
    print("Can you guess my secret?")
    # put your code here
    while True:
        userInput = int(input("Input a number between 1 and 100: "))
        if userInput == secret:
            print(f"\nYou won! The number was {secret}!")
            break
        elif userInput < secret:
            print(f"\nYour guess ({userInput}) was too low! Please try again.")
        else:
            print(f"\nYour guess ({userInput}) was too high! Please try again.")


main()
