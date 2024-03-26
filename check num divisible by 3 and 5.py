"""
Check for Divisibility by 3 AND 5:
Write a python function to check if a given number is divisible by both 3 and 5.
Sample Data:
Number: 15
"""
in_num = int(input("Enter a number:- "))
if in_num % 3 == 0 and in_num % 5 == 0:
    print("A given number is divisible by both 3 and 5.")
else:
    print("A given number is not divisible by both 3 and 5.")