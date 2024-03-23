"""To print the following series. 5*4,5*3,5*2,......5*(-12)
(Print in two ways – patter & multiplied value) """

num = 5
i = 4
while i >= -12:
    print(f"{num} * {i} = ", num * i)
    i -= 1