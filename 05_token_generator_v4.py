# component 3 (generating random tokens) 4.0
# Calculate user balance on random selection of tokens

import random

# Showing staring balance.
STARTING_BALANCE = 10
# Set balance variable as STARTING_BALANCE to make calculation easier
balance = STARTING_BALANCE

# Testing in range of 100 times
for item in range(100):
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
    print(f"Token: {token}, Balance: ${balance}")


# Showing Starting balance, and Final balance to see whether they lost money or win.
print(f"Starting balance: {STARTING_BALANCE:.2f}")
print(f"Final balance: {balance:.2f}")





