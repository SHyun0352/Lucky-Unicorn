# component 3 (generating random tokens) 3.0
# Calculate user balance on random selection of tokens

import random

STARTING_BALANCE = 10
balance = STARTING_BALANCE


for item in range(100):
    number = random.randint(1, 100)

    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4

    elif 6 <= number <= 36:
        token = "donkey"
        balance -= 1

    else:
        if number % 2 == 0:
            token = 'zebra'
            balance -= 0.5
        else:
            token = 'horse'
            balance -= 0.5
    print(f"Token: {token}, Balance: ${balance}")


print(f"Starting balance: {STARTING_BALANCE:.2f}")
print(f"Final balance: {balance:.2f}")





