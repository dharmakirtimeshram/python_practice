"""
Check square of entered number is even  and divisible by 4
"""
num = int(input("Enter a number :- "))
sqr = num*num
if sqr%2 == 0 and sqr%4==0:
    print(f"Square of {num} >> {sqr}. This is even number and divisible by 4.")
else:
    print(f"Square of {num} >> {sqr}. This is not even number and divisible by 4.")
