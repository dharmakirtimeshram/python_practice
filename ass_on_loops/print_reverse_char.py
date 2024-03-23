#Print the characters of a string in reverse order using a "for" loop.

user_input = input("Enter string value - ")

for i in range(len(user_input)-1, -1, -1):
        print(user_input[i], end="")



