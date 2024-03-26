"""
Check for Divisibility by 4 OR 6:
Create a python function to check if a given number is divisible by either 4 or 6.
Sample Data:
Number: 24
"""

def check_num(x):
    if x%4 == 0 or x%6 == 0:
        print("A given number is divisible by either 4 or 6.")
    else:
        print("A given number is not divisible by 4 or 6.")


in_num = int(input("Enter a number :- "))
check_num(in_num)