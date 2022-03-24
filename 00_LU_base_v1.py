"""LU base component
Components added after they have been created and tested"""


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


# Main routine
played_before = verification("Have you played this game before? (yes/no): ")

if played_before == "No":
    instruction()

user_balance = num_check("How much would you like to play with $", 1, 10)
print(f"You are playing with ${user_balance}")
