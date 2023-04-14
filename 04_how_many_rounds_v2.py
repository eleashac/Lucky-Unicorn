"""
Lucky Unicorn - How many rounds v2
uses try/accept loop to prevent crashes if input is not an integer
Created by Eleasha Chan
"""

error = "Please enter a whole number between 1 and 10\n"
valid = False

# keep asking until a valid amount (1-10) is entered
while not valid:
    try:
        # ask for amount
        user_balance = int(input("How many rounds would you like to play? "
                                 "($1 per round - must be between 1 and 10): "))

        # check if amount is too high or low
        if 0 < user_balance <= 10:
            print(f"You are playing with ${user_balance}")
            valid = True
        else:
            print(error)

    except ValueError:
        print(error)
