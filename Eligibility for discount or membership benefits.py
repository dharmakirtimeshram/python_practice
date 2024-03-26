"""
Eligibility for Discount OR Membership Benefits:
Create a python program to check if a customer is eligible for a discount (purchase amount greater
than 200) or qualifies for membership benefits (loyalty card available).
Sample Data:
Purchase Amount: 180
Loyalty Card: true
"""
purchase_amount = int(input("Enter your purchase amount:- "))
loyalti_card = input("Enter loyalty card status:- ")

if purchase_amount >= 200 or loyalti_card == True:
    print("A customer is eligible for a discount or qualifies for membership benefits.")
else:
    print("A customer is not eligible for a discount or qualifies for membership benefits.")
