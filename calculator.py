"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

# get input
# split by spaces
# convert to int
# run relevant function in arithmetic.py
# print result


from arithmetic import *
import functools


while True:
    user_command = input(">")
    # allowing to quit out of calculator
    if user_command == "q" or user_command == "quit":
        print("Good bye.")
        break
    # tokenizing user input
    commands = user_command.split()
    numbers = [float(i) for i in commands[1:]]
    operator = commands[0].lower()
    num1 = float(commands[1])

    # calling functions in aritmetic.py
    if operator == "+":
        print(round(functools.reduce(add, numbers), 3))
    elif operator == "-":
        print(round(functools.reduce(subtract, numbers), 3))
    elif operator == "*":
        print(round(functools.reduce(multiply, numbers), 3))
    elif operator == "/":
        print(round(functools.reduce(divide, numbers), 3))
    elif operator == "square":
        print(round(square(num1), 3))
    elif operator == "cube":
        print(round(cube(num1), 3))
    elif operator == "pow":
        print(round(functools.reduce(power, numbers), 3))
    elif operator == "mod":
        print(round(functools.reduce(mod, numbers), 3))
    else:
        print("um. that's not a valid operator.")
        print("try again. K thanks.")
