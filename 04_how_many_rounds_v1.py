"""
Lucky Unicorn - How many rounds v1
changing 04_how_many_rounds_v3 into a function
asks user how many rounds they want to play and checks the input is between 1
and 10. If so, this amount becomes the balance in their account ($1 per round)
Created by Eleasha Chan
"""

user_balance = int(input("How many rounds would you like to play? ($1 per round"
                         " - must be between 1 and 10): "))

# keep asking until a valid amount (1-10) is entered
while user_balance < 1 or user_balance > 10:
    # print("Please enter a whole number between 1 and 10")
    # ask for input
    user_balance = int(input("Please enter a whole number between 1 and 10: "))

print(f"You are playing with ${user_balance}")
