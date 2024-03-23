'''
Declare and initialize 3 three variable and print the biggest number
'''

num1 =int(input("Enter first variable:- "))
num2 =int(input("Enter second variable:- "))
num3 =int(input("Enter third variable:-  "))
print("Variables-- (" ,num1,num2,num3, ")")
if(num1>num2 and num1>num3):
    print(f"{num1} :- is the biggest number")
elif(num2>num1 and num2>num3):
    print(f" {num2} :- is the biggest number")
else:
    print(f"{num3} :- is the biggest number")