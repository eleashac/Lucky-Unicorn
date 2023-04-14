"""
Lucky Unicorn - How many rounds function
also needed to change user_balance to the more generic variable name 'response'
and to change the condition and position of the number comparison into the loop
to make the function recyclable
Created by Eleasha Chan
"""


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
user_balance = num_check("How many rounds would you like to play? "
                         "($1 per round - must be between 1 and 10): ", 1, 10)
print(f"You are playing with ${user_balance}")
