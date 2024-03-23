#Check if a given number is a perfect square using a "while" loop.

user_input = int(input("Enter number :-  "))

i = 1
while i <= user_input:
    if user_input / i == i:
        print(user_input, "- Is a square of ", i)
        print("Perfect square")
        break
    i += 1
else:
    print("Not a perfect square")