"""
Lucky Unicorn - based on 00_LU_base_v1
Components added after they have been created and tested
Created by Eleasha Chan
"""

import random


# yes/no check function
def yes_no(question_text):
    while True:

        # Ask user if they know how to play Lucky Unicorn
        answer = input(question_text).lower()

        while answer != "yes" and answer != "no" and \
                answer != "y" and answer != "n":
            print("Please enter yes or no ")

            answer = input(question_text).lower()

        # If they say yes, output 'Program Continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'Display instructions'
        else:
            answer = "No"
            return answer


# display instructions function
def instructions():
    print("\n***** How to play Lucky Unicorn *****\n")
    print("The rules of the game will go here\n")


# number checking function
def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    # keep asking until a valid amount (1-10) is entered
    while True:
        try:
            # ask for amount
            response = int(input(question))

            # check number is within required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# function to generate random token
def generate_token(balance):

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
    return balance


# main routine
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()


# ask user how much they want to play with
starting_balance = num_check("How many rounds would you like to play? ($1 per "
                             "round - must be between 1 and 10): ", 1, 10)
print(f"You are playing with ${starting_balance}\n")

closing_balance = generate_token(starting_balance)
print(f"Starting balance = ${starting_balance:.2f}\n"
      f"Final balance = ${closing_balance:.2f}")
print("\nThanks for playing!")
