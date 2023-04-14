"""
Lucky Unicorn - Yes/No check function
based on 01_yes_no_v3
Created by Eleasha Chan
"""


# functions
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


# main routine
show_instructions = yes_no("Have you played this game before? ")
print(f"You have entered {show_instructions}")

print()

having_fun = yes_no("Are you having fun? ")
print(f"You have entered {having_fun}")
