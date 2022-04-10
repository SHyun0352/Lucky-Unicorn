# component 3 (generating random tokens)

import random

tokens = ["unicorn", "horse", "donkey", "zebra"]

for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')


