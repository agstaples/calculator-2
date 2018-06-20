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
        command_list = user_command.split(" ")
        operator = command_list[0]
        num1 = int(comman_list[1])
        if len(command_list) >= 3:
            num2 = int(command_list[2])
        if len(command_list) == 4:
            num3 = int(command_list[3])

        if user_command == "q" or user_command == "quit":
            print("Good bye.")
            break

        if operator == ""
