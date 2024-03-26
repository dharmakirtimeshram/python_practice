"""
Check for Multiple of 3 AND 7:
Implement a python function to check if a given number is both a multiple of 3 and 7.
Sample Data:
Number: 21
"""
def mult(x):
    if x%3 == 0 and x%7 == 0:
        print(f"{x} is a multiple of both  3 and 7.")
    else:
        print(f"{x} is not a multiple of both 3 and 7.")

in_num = int(input("Enter a number:- "))
mult(in_num)


