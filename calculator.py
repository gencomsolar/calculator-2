"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *
# import arithmetic

while True:
    user_input = raw_input(">")
    nums = user_input.split(" ")
    if nums[0] == "q":
        break
    #um1 = int(tokens[1])
    #f len(tokens) == 3:
    #   num2 = int(tokens[2])
    if nums[0] == "+":
        print add(nums)
    elif tokens[0] == "-":
        print subtract(num1, num2)
    elif tokens[0] == "/":
        print divide(num1, num2)
    elif tokens[0] == "*":
        print multiply(num1, num2)
    elif tokens[0] == "square":
        print square(num1)
    elif tokens[0] == "cube":
        print cube(num1)
    elif tokens[0] == "pow":
        print pow(num1, num2)
    elif tokens[0] == "mod":
        print mod(num1, num2) 