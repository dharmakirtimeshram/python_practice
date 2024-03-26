"""
Check for Odd AND  Divisible by 5:
Create a python program to check if a given number is both odd and divisible by 5.
Sample Data:
Number: 15
"""
in_num = int(input("Enter a number :-"))
if in_num % 2 != 0 and in_num % 5 == 0:
    print("A given number is both odd and divisible by 5.")
else:
    print("A given number is not both odd and divisible by 5.")


