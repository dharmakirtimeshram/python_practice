#Check if a string is a palindrome using a "for" loop.

user_input = input("Enter your string variable :- ")
rev = ""

for i in range(len(user_input)-1, -1, -1):
      rev += user_input[i]

if user_input == rev:
    print("It is palindrome")
else:
    print("It is not palindrome")
