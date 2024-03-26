"""
Check for Non-Positive AND Even Number:
Implement a python program to check if a given number is both non-positive and even.
Sample Data:
Number: -6
"""

in_num = int(input("Enter a number :- "))
num = in_num * -1
if in_num < num and in_num % 2 == 0:
    print("A given number is both non-positive and even.")
else:
    print("A given number is not both non-positive and even")
