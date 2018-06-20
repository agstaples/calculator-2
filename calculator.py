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


def calculate():
    """takes in numbers and commands and calculates answer"""
    
    while True:
        user_command = input(">")
        # tokenizing user input
        command_list = user_command.split(" ")
        operator = command_list[0].lower()
        num1 = float(command_list[1])      
        # accounting for inputs of different lengths
        if len(command_list) >= 3:
            num2 = float(command_list[2])
        if len(command_list) == 4:
            # num3 = float(command_list[3])
            print("We are going to use your first 2 lovely numbers.")

        # allowing to quit out of calculator
        if user_command == "q" or user_command == "quit":
            print("Good bye.")
            break
        # calling functions in aritmetic.py
        if operator == "+":
            print(add(num1, num2))
        elif operator == "-":
            print(subtract(num1, num2))
        elif operator == "*":
            print(multiply(num1, num2))
        elif operator == "/":
            print(divide(num1, num2))
        elif operator == "square":
            print(square(num1))
        elif operator == "cube":
            print(cube(num1))
        elif operator == "pow":
            print(power(num1, num2))
        elif operator == "mod":
            print(mod(num1, num2))
        else:
            print("um. that's not a valid operator.")
            print("try again. K thanks.")

calculate()