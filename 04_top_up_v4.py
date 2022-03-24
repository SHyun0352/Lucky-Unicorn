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
user_balance = num_check("How much would you like to play with $", 1, 10)
print(f"You are playing with ${user_balance}")
