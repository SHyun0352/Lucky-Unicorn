# component 3 (generating random tokens) 2.0
# Calculate user balance on random selection of tokens

import random

tokens = ["unicorn", "horse", "donkey", "zebra", "horse", "horse", "donkey", "donkey", "zebra", "zebra"]
STARTING_BALANCE = 10
balance = STARTING_BALANCE


for item in range(100):
    token = random.choice(tokens)

    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= 0.5

print(f"Starting balance: {STARTING_BALANCE:.2f}")
print(f"Final balance: {balance:.2f}")




