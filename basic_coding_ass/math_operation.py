
"""Write a program to perform simple math based on the user inputs by using
Switch condition.(+ , - , * , /) """

x = int(input("Enter your first value - "))
y = int(input("Enter your second value - "))
cmd = input("operation:- ")

if cmd == "+":
    add = x + y
    print(f"{x}+{y}={add}")
elif cmd == "-":
    sub = x - y
    print(f"{x}-{y}={sub}")
elif cmd == "*":
    mul = x * y
    print(f"{x}*{y}={mul}")
elif cmd == "/":
    if y == 0:
        print("Error,invalid input")
    else:
        div = x / y
        print(f"{x}/{y}={div}")
else:
    print("Invalid operation")
