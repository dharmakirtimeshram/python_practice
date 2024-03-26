"""
Divisibility by 3 OR 8:
Write a python function to check if a given number is divisible by either 3 or 8.
Sample Data:
Number: 24
"""
def check_num(x):
    if x%3 == 0 or x%8 == 0:
        print("A given number is divisible by either 3 or 8")
    else:
        print("A given number is not divisible by 3 or 8")


num = int(input("Enter a number :-  "))
check_num(num)

