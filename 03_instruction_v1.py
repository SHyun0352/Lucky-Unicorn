"""
evolving! ! !
"""


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
    print("Program continues")
    print()


# Main routine
played_before = verification("Have you played this game before? (yes/no): ")

if played_before == "No":
    instruction()

else:
    print("Program continues")
