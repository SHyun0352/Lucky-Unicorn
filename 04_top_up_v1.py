"""Component 2
Ask player how much are they going to play with, if the number is invalid, request to answer again.
if the number is valid, set the amount as user_balance"""

user_balance = int(input("How much do you want to play with (must be an integer between 1 and 10) $"))

while not 1 <= user_balance <= 10:
    print("Try again, Please enter a whole number between 1 and 10")

    user_balance = int(input("How much do you want to play with (must be an integer between 1 and 10) $"))

print(f"You are playing with ${user_balance}")
