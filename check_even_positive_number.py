"""
Check for Even AND Positive Number:
Write a python function to check if a given number is both even and positive.
Sample Data:14
"""

num = int(input("Enter number:- "))

def check(x):
  pn = x * -1
  if x > pn and x%2 == 0:
      print(f"{x} :- This number is both even and positive ", end="")
  else:
      print(f"{x} :- This number is not both even and positive", end="")

test = check(num)