"""
Divisibility by 5 OR 9:
Write a python program to check if a given number is divisible by either 5 or 9.
Sample Data:
Number: 45
"""

in_num = int(input("Enter a number :- "))
if in_num % 5 == 0 or in_num % 9 == 0:
    print("A given number is divisible by either 5 or 9.")
else:
    print("A given number is not divisible by 5 or 9.")