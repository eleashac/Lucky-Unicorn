"""
Lucky Unicorn - based on 00_LU_base_v3
Edited for increased user clarity and enjoyability - feedback from family
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
    print()
    print(formatter("-", "How to Play"))
    print()
    print("First choose a starting amount to play with - "
          "must be between $1 and $10.")
    print("Then press <enter> to play. You will win a random token: "
          "either a horse, zebra, donkey, or unicorn.")
    print()
    print("It costs $1 to play each round. These are the payout amounts:\n"
          "\tUnicorn: WIN $5!\n"
          "\tHorse: WIN $0.50 \n"
          "\tZebra: WIN $0.50 \n"
          "\tDonkey: $0.00 ")
    print()
    print("You have the opportunity to end the game and cash in your rewards "
          "anytime by entering 'X'. See if you can avoid donkeys, win unicorns,"
          "and finish with more money than you started with! \n")
    print("*" * 50)
    print()


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
        print(f"Round {rounds_played} \n")
        number = random.randint(1, 100)

        # adjust balance
        # if the random number is between 1 and 5 user gets a unicorn
        # (add $4 to balance)
        if 1 <= number <= 5:
            balance += 4
            print(formatter("*", "Congratulations, you won a Unicorn!"))
            print()

        # if the random number is between 1 and 5 user gets a unicorn
        # (subtract $1 from balance)
        elif 6 <= number <= 36:
            balance -= 1
            print(formatter("D", "Bad luck, you got a Donkey"))
            print()

        # in all other cases the token must be a horse or zebra
        # (subtract $0.50 in either case)
        # if the number is even, set token to zebra
        else:
            if number % 2 == 0:
                balance -= 0.50
                print(formatter("Z", "You won a Zebra"))
                print()

            # if the number is odd, set token to horse
            else:
                balance -= 0.50
                print(formatter("H", "You won a Horse"))
                print()

    # output
        print(f"Your balance is now: ${balance:.2f}")
        if balance < 1:
            print("\nSorry, but you have run out of money")
            play_again = "x"
        else:
            play_again = input("\nDo you want to play another round?\nPress "
                               "<enter> to play again or 'X' to exit ").lower()
        print()
    return balance


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# main routine
print(formatter("=", "Welcome to the Lucky Unicorn Game"))
print()

played_before = yes_no("Have you played this game before? y/n: ")

if played_before == "No":
    instructions()


# ask user how much they want to play with
starting_balance = num_check("How much money would you like to play with?"
                             " 1 - 10 dollars: $", 1, 10)
print(f"You are playing with ${starting_balance}\n")

closing_balance = generate_token(starting_balance)
print(f"Starting balance: ${starting_balance:.2f}\n"
      f"Final balance: ${closing_balance:.2f}")
print()
print(formatter("=", "Thanks for playing!"))
