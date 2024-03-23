'''
Write a program to print all numbers which are divisible by 11 from 250 to 550.
'''



print("Numbers which are divisible by 11 from 250 to 550")
i = 250
while i <= 550:
    if i % 11 == 0:
        print(i)
    i += 1