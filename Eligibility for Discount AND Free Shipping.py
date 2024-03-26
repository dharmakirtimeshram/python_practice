"""
Eligibility for Discount AND Free Shipping:
Create a python program to check if a customer is eligible for a discount (purchase amount greater
than 150) and qualifies for free shipping (purchase amount greater than 100).
Sample Data:
Purchase Amount: 120
"""

purchase_amount =int(input("Enter a purchase amount :- "))

if purchase_amount >= 100:
    print("A customer is qualifies for free shipping", end="")
    if purchase_amount >=150:
        print(" and eligible for a discount.")
else:
    print("Add more item for free shipping.")