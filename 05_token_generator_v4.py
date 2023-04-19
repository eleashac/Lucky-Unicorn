"""
Lucky Unicorn - token generator v3
Calculate percentages to ensure the odds favour the house
5% unicorns, 30% donkeys, and the remaining 65% horses/zebra
Created by Eleasha Chan
"""

import random

STARTING_BALANCE = 100
balance = STARTING_BALANCE

# Testing loop to generate 10 tokens
for item in range(1000):
    number = random.randint(1, 100)

    # adjust balance
    # if the random number is between 1 and 5 user gets a unicorn
    # (add $4 to balance)
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4

    # if the random number is between 1 and 5 user gets a unicorn
    # (subtract $1 from balance)
    elif 6 <= number <= 36:
        token = "donkey"
        balance -= 1

    # in all other cases the token must be a horse or zebra
    # (subtract $0.50 in either case)
    # if the number is even, set token to zebra
    else:
        if number % 2 == 0:
            token = "zebra"
            balance -= 0.50

        # if the number is odd, set token to zebra
        else:
            token = "horse"
            balance -= 0.50

# output
    print(f"Token: {token}, Balance: ${balance}")

print(f"\nStarting balance = ${STARTING_BALANCE:.2f}\n"
      f"Final balance = ${balance:.2f}")
