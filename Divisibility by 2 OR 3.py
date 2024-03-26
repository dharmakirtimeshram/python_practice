"""
Divisibility by 2 OR 3:
Write a python function to check if a given number is divisible by either 2 or 3.
Sample Data:
Number: 9
"""

def check_num(x):
    if x%2 ==0 or x%3 == 0:
        print("A given number is divisible by either 2 or 3.")
    else:
        print("A given number is not divisible by 2 or 3.")


in_num =int(input("Enter a number:- "))
check_num(in_num)
