"""
Lucky Unicorn - Instructions
uses function from 01_yes_no_function_v1 to create new function which
incorporates both yes/no and show instructions
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
    print("Program Continues\n")


# main routine
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()
else:
    print("Program Continues")
