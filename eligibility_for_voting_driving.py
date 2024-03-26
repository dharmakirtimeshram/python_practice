"""
Eligibility for Voting OR Driving:
Create a python program to check if a person is eligible to vote (age greater than or equal to 18) or
eligible to drive (age greater than or equal to 16).
Sample Data:
Age: 20

"""
age = int(input("Enter age :- "))

if age >= 16 or age >= 18:
    print("A person is eligible to vote or drive ")
else:
    print("A person is not eligible for to vote or drive")


