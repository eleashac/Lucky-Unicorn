"""
Lucky Unicorn - How many rounds v3
more efficient method, includes valid range as the basis of the while loop which
eliminates the need to use the 'valid' variable
Created by Eleasha Chan
"""

error = "Please enter a whole number between 1 and 10\n"
user_balance = 0

# keep asking until a valid amount (1-10) is entered
while not 0 < user_balance <= 10:
    try:
        # ask for amount
        user_balance = int(input("How many rounds would you like to play? "
                                 "($1 per round - must be between 1 and 10): "))

        print()

    except ValueError:
        print(error)

print(f"You are playing with ${user_balance}")