# To print the count of the even numbers between the given range (1 - 20).

count = 0
i: int = 1
while i <= 20:
    if i % 2 == 0:
        count = count + 1
    i = i + 1
print(count)
