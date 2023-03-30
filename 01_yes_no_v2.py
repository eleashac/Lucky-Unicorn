"""
Lucky Unicorn - Yes/No check v2
simplifies the input by converting it to lower case. Also accepts
y or n as abbreviations. Prints result of user choice and input - for testing
Created by Eleasha Chan
"""


# Ask user if they know how to play Lucky Unicorn
show_instructions = input("Do you know how to play Lucky Unicorn? yes/no: "
                          ).lower()

# If they say yes, output 'Program Continues'
if show_instructions == "yes":
    print("Program Continues")

# If they say no, output 'Display instructions'
elif show_instructions == "no":
    print("Display instructions")

# Otherwise, show error
else:
    print("Please enter yes or no")

print(f"You have entered {show_instructions}")
