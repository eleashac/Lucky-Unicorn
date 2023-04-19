"""
Lucky Unicorn - token generator v3
format currency
ensures odds favour the house: 10% chance of unicorn, 30% chance each for
donkey, zebra, and horse
Created by Eleasha Chan
"""

import random

tokens = ["unicorn",
          "horse", "horse","horse",
          "donkey", "donkey","donkey",
          "zebra","zebra","zebra"]

STARTING_BALANCE = 100
balance = STARTING_BALANCE

# Testing loop to generate 20 tokens
for item in range(100):
    token = random.choice(tokens)

    # adjust balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= 0.50

# output
print(f"Starting balance = ${STARTING_BALANCE:.2f}\n"
      f"Final balance = ${balance:.2f}")
