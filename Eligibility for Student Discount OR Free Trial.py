"""
Eligibility for Student Discount OR Free Trial:
Write a python program to check if a person is eligible for a student discount (age less than 25) or is
eligible for a free trial.
Sample Data:
Age: 22
Free Trial: true
"""
age = int(input("Enter a age :- "))
free_trial = input("Status of free trail :- ")

if age <= 25 or free_trial == True:
    print("A person is eligible for a student discount or for a free trial")
else:
    print("A person is not eligible for a student discount or for a free trial")