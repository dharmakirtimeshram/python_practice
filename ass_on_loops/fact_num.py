#The factorial of a given number using a "for" loop.

user_input = int(input("Enter number:- "))
fact = 1
for i in range(user_input, 0 , -1):
    fact = fact*i
print(f"Factorial of {user_input} :- {fact} ")