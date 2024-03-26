"""
Check for Odd OR Prime Number:
Write a python function to check if a given number is either odd or a prime number.
Sample Data:
Number: 11
"""


def odd_prime(x):
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1

    if count == 2 or x % 2 != 0:
        print("A given number is either odd or a prime number.")
    else:
        print("A given number is not odd or a prime number.")


in_num = int(input("Enter a number :- "))
odd_prime(in_num)