"""
Lucky Unicorn - game mechanics and looping v2
Removed hard-wiring so that all tokens can be allocated (randint 1-100)
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
    print(f"Round {rounds_played}. Token: {token}, Balance: ${balance}")
    if balance < 1:
        print("\nSorry, but you have run out of money")
        play_again = "x"
    else:
        play_again = input("\nDo you want to play another round?\nPress "
                           "<enter> to play again or 'X' to exit ").lower()
    print()

print(f"Starting balance = ${TEST_AMOUNT:.2f}\n"
      f"Final balance = ${balance:.2f}")
print("\nThanks for playing!")
