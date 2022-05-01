""" Component 4 - Looping rounds. Loop_Rounds_v2
Converting into def(function).
"""

import random


# Function to generate random tokens
def generate_token(balance):
    rounds_played = 0
    play_again = ""

    while play_again != "x":
        rounds_played += 1
        number = random.randint(1, 100)

        # Setting percentage of 'Unicorn' to 5 percent.
        if 1 <= number <= 5:
            token = "unicorn"
            balance += 4

        # 'Donkey' has 30 percent chance to be shown.
        elif 6 <= number <= 36:
            token = "donkey"
            balance -= 1

        # 'Zebra' and 'Horse' has same percentage to be shown.
        # However, if the number is even, 'Zebra' is selected.
        # if the  number is odd, 'Horse' is selected.
        else:
            if number % 2 == 0:
                token = 'zebra'
                balance -= 0.5
            else:
                token = 'horse'
                balance -= 0.5

        print(f"Round {rounds_played}. Token = {token}, Balance = {balance}.")
        if balance < 1:
            print("\nSorry, you have run out of money.")
            play_again = "x"
        else:
            play_again = input("\nDo you want to play another round?\n<enter> to play again or 'X' to exit ").lower()
            print()
    return balance


starting_balance = 5
closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"You finished with ${closing_balance:.2f}")
print("Goodbye")


