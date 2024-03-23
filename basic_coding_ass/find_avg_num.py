# To find the average of 24,26,28,.....100.

i = 24
count = 0
sum = 0
while i <= 100:
    count = count + 1
    sum = sum + i
    i = i+1
avg = sum/count
print("Average:- ", avg)
