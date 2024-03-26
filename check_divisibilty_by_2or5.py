"""
Check for Divisibility by 2 OR 5:
Write a python function to check if a given number is divisible by either 2 or 5.
Sample Data:
Number: 25
"""
def check_num(x):
    if x%2 == 0 or x%5 == 0:
        print("A given number is divisible by either 2 or 5.")
    else:
        print("A given number is not divisible by 2 or 5.")

in_num = int(input("Enter number:- "))
check_num(in_num)