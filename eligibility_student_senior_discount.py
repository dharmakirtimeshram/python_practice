"""
Eligibility for Senior Discount OR Student Discount:
Create a python program to check if a person is eligible for a senior citizen discount
 (age greater than 60) or a student discount (age less than 25).
Sample Data:
Age: 63
"""
age = int(input("Enter age:- "))
if age < 25 or age > 60:
    print("A person is eligible for a senior citizen discount or a student discount ")
else:
    print("A person is not eligible for a senior citizen discount or a student discount ")