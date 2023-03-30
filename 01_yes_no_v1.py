# Ask user if they know how to play
show_instructions = input("Do you know how to play Lucky Unicorn? yes/no: ")

# If they say yes, output 'Program Continues'
if show_instructions == "yes":
    print("Program Continues")

# If they say no, output 'Display instructions'
elif show_instructions == "no":
    print("Display instructions")

# Otherwise, show error
else:
    print("Please enter yes or no")
