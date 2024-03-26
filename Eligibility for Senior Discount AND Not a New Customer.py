"""
Eligibility for Senior Discount AND Not a New Customer:
Create a python program to check if a person is eligible for a senior citizen discount (age greater than
65) and is not a new customer.
Sample Data:
Age: 70
New Customer: false
"""
age = 70
new_customer = False

if age > 65 and new_customer == False:
    print("A person is eligible for a senior citizen discount. ")
else:
    print("A person is not eligible for a senior citizen discount. ")