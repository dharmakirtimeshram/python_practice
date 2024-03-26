"""
Odd Number Check with AND:
Implement a python function to check if a given number is odd and not divisible by 3.
Sample Data:
Number: 27

"""
user_input = int(input("Enter number :-  "))

def check_num(x):
    if x % 3 != 0 and x % 2 != 0:
        print("Given number is odd number and not divisible by 3")
    else:
        print("Condition not satisfied by given number ")

num = check_num(user_input)