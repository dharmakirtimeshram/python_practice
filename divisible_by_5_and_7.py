"""
Divisibility by 5 AND 7:
Write a python function to check if a given number is divisible by both 5 and 7.
Sample Data:
Number: 35
"""


def divide_check(x):
    if x % 5 == 0 and x % 7 == 0:
        print("A given number is divisible by both 5 and 7")
    else:
        print("A given number is not divisible by both 5 and 7")

num = int(input("Enter number :-  "))
num2 = divide_check(num)