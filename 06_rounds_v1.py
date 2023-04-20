"""
Lucky Unicorn - game mechanics and looping v1
Based on 05_token_generator_v4 but hard-wired to only allocate donkeys
Gives user feedback about number of rounds and maintains balance
Test amount set to $5
"""


import random

# Main routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ""

# Testing loop to generate 5 tokens
while play_again != "x":
    rounds_played += 1  # keep track of rounds
    number = random.randint(6, 36)

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
