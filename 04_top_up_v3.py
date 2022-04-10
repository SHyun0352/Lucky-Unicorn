error = "Please enter a whole number between 1 and 10\n"
user_balance = 0

while not valid:
    try:
        user_balance = int(input("Please enter a whole number between 1 and 10" 
                                 "\nHow much are you going to play with? $: "))
        print()

    except ValueError:
        print(error)

print(f"You are playing with ${user_balance}")
