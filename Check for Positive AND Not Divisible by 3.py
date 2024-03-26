"""
Check for Positive AND Not Divisible by 3:
Implement a python program to check if a given number is positive and not divisible by 3.
Sample Data:
Number: 7
"""
in_num = int(input("Enter a number :- "))
num = in_num * -1
if in_num > num and in_num%3 != 0:
    print("A given number is positive and not divisible by 3.")
else:
    print("condition not satisfied")
