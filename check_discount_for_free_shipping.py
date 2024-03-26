"""
Eligibility for Discount OR Free Shipping:
Create a python program to check if a customer is eligible for a discount (purchase amount greater
than 150) or qualifies for free shipping (purchase amount greater than 100).
Sample Data:
Purchase Amount: 120
"""

purchase_amount = int(input("Enter your amount:- "))
if purchase_amount >= 150 or purchase_amount >= 100:
    print("congratulations!!", end="")
    if purchase_amount >= 100:
        print("You are Qualifies for free shipping", end="")
    elif purchase_amount >= 150:
        print("You are Eligible for discount",end="")
else:
    print("Add more item for free shipping")
