"""
Check for Non-Negative AND Not Divisible by 7:
Implement a python program to check if a given number is non-negative and not divisible by 7.
Sample Data:
Number: 14
"""
in_num = int(input("Enter a number:- "))
num= in_num * -1
if in_num > num and in_num%7 != 0:
    print("A given number is non-negative and not divisible by 7.")
else:
    print("Not satisfied given condition.")
