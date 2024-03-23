# To sum all even numbers between 382 and 582.


i = 382
sum_even = 0
while i <= 582:
    if i % 2 == 0:
        sum_even = sum_even + i
    i = i + 1
print(sum_even)
