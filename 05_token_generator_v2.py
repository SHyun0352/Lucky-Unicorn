# component 3 (generating random tokens) 2.0
# Calculate user balance on random selection of tokens

import random

tokens = ["unicorn", "horse", "donkey", "zebra"]
response = 10


for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')

    if token == "unicorn":
        response += 4
    elif token == "donkey":
        response -= 1
    else:
        response -= 0.5

    print(f"What you win: {token}, Balance: ${response}")




