"""
Lucky Unicorn - Base
components added after they have been created and tested
Created by Eleasha Chan
"""


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


# main routine
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()


# ask user how much they want to play with
user_balance = num_check("How many rounds would you like to play? "
                         "($1 per round - must be between 1 and 10): ", 1, 10)
print(f"You are playing with ${user_balance}")
