"""LU base component
Components added after they have been created and tested"""


import random


# checks whether player types correct answer(yes/no)
def verification(question_text):
    while True:

        answer = input(question_text).lower()
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        else:
            print("Please enter valid answer. (yes/no)")


def instruction():
    print("**** How to Play ****")
    print()
    print("The rules of the game goes here")
    print()


def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)

    while True:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


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
            print(formatter("!", "Congratulations, you got Unicorn"))
            print()

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


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main routine
print(formatter("-", "Welcome to the Lucky Unicorn game"))
print()
played_before = verification("Have you played this game before? (yes/no): ")

if played_before == "No":
    instruction()


starting_balance = num_check("How much would you like to play with $", 1, 10)
print(f"You are playing with ${starting_balance}")

closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"You finished with ${closing_balance:.2f}")
print()
print(formatter("*", "Goodbye"))
