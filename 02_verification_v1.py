"""
evolving! ! !
"""
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


# Main routine
question = input("Have you played this game before? (yes/no): ")
print(f"You have chosen {question}.")
print()
chill = verification("Are you having fun? ")
print(f"You entered {chill}")
