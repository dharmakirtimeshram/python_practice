# Print series 2*3,3*4,4*5,......16*17 (Print in two ways – pattern & multiplied value)

i = 2
j = 3
k = 0
while i <= 16:
    k = i * j
    print(f"{i} * {j} = {k}")
    i = i + 1
    j = j + 1

