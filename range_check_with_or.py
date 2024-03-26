"""
Range Check with OR:
Create a python program to determine if a given value is either less than -10 or greater than 10.
Sample Data:
Value: -15
"""

user_input = int(input("Enter Number:- "))

if user_input < -10 or user_input > 10:
    print("Given value is either less than -10 or greater than 10 ")
else:
    print("given number is not less than -10 or greater than 10 ")
