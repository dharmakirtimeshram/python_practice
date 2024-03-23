#Check prime number using while loop

in_num = int(input("Enter any number :- "))
count = 0
i = 1
while in_num >= i:
    if in_num % i == 0:
        count = count + 1
    i += 1
if count == 2:
    print("prime number")
else:
    print("not prime")
