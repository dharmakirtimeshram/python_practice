#Count the number of vowels in a given string using a "for" loop.

user_input = input("Enter string variable :- ")
user_input2 = user_input.lower()
vowels = "aeiou"

count = 0
for i in range(0, len(user_input2)):
    if user_input2[i] in vowels:
        count += 1
print(count)