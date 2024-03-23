""" To print the following series. 1,even,3,even,5,even,.......35,even"""

i = 1
while i <= 36:
    if i % 2 == 0:
        print("even", end =" ")
    else:
        print(i, end=" ")
    i += 1