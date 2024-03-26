"""
Check for Non-Negative OR Even Number:
Create a python program to check if a given number is either non-negative or even.
Sample Data:
Number: -8

"""
user_input =int(input("Enter number:- "))
num2 = user_input * -1
if num2 < user_input or user_input % 2 == 0:
    print("A given number is either non-negative or even ")
else:
    print("A given number is not even or non-negative ")