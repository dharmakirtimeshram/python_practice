"""
Inverted Triangle Pattern:
* * * * *
* * * *
* * *
* *
*

"""

for i in range(5, -1, -1):
    for j in range(0, i+1):
        print("*",end=" ")
    print()