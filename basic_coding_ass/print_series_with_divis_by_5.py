""" To print the following series. 1,3, divisible by five, 7,9,
11,13, divisible by five,.....21,23, divisible by five"""

i = 1
while i <= 25:
    if i % 2 != 0:
        if i % 5 != 0:
            print(i)
        else:
            print("Divisible by five")
    i += 1

