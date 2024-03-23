"""To print the following series. 1,2,factor of three,4,5,factor
of three, 7,8,factor of three,..........22,23,factor of three."""

i = 1
while i <= 24:
    if i % 3 == 0:
        print("factor of three ")
    else:
        print(i)
    i += 1








