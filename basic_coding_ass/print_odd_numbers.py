# To print all odd numbers from 251 to 51. like (251, 249,...51).

i = 251
while i >= 51:
    if i % 2 != 0:
        print(i)
    i = i - 1
