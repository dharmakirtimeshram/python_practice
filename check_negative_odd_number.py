"""
Check for Negative AND Odd Number:
Implement a python program to check if a given number is both negative and odd.
Sample Data:
Number: -7
"""
user_input = int(input("Enter number :- "))
user_num = user_input * -1
if user_num > user_input and user_num % 2 != 0:
    print("A given number is both negative and odd")
else:
    print("A given number is not both negative and odd")