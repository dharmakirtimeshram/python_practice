"""
Multiple Range Check:
Write a python function to check if a given number is in the range [1, 10] or [20, 30].
Sample Data:
Number: 25
"""

user_input = int(input("Enter any number:- "))
if user_input >=1 and user_input <= 10 or user_input >= 20 and user_input <= 30:
    print("Number is in range [1,10 ] or [20,30] ")
else:
    print("Number is not in range [1,10 ] or [20,30] ")