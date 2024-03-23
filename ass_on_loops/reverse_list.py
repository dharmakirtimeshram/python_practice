#Print the elements of a list in reverse order using a "for" loop.

lst = [10, 20, 30, 40, 50, 60, 70]
for i in range(len(lst)-1, -1, -1):
    print(lst[i])