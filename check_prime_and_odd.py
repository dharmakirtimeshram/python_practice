"""
)Check for Prime AND Odd Number:
Write a python function to check if a given number is both a prime number and an odd number.
Sample Data:
Number: 17
"""

def check_num(x):
    count = 0
    for i in range(1, x+1):
        if x % i == 0:
            count += 1
    
    if count == 2 and x%2 != 0:
        print("A given number is both prime number and odd number")
    else:
        print("A given number is not both prime number and odd number")


user_num = int(input("Enter number:- "))
check_num(user_num)