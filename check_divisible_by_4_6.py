"""
Divisibility by 4 OR 6:
Write a python program to check if a given number is divisible by either 4 or 6.
Sample Data:
Number: 18
"""

user_input = int(input("enter Number :-  "))

if user_input % 4 == 0 or user_input % 6 == 0:
    print("Given number is divisible by either 4 or 6  ")
else:
    print("Given number is not divisible by 4 or 6")