'''
 performs the following tasks.
 a. Store a number in a variable
 b. If value is not in range (100-1000) prints wrong number else follows the steps
 c. Check even or odd
 d. If even divide the number by 3 and print the remainder
 e. If odd divide the number by 2 and print the remainder

'''

num = int(input("Enter number:- "))

if(num<100 or num>1000):

    print(num, " Wrong number")

else:
  print("Number is in Range (100-1000)")
  if(num%2==0):
            print(num,"- Even number")
            evn_rem=num%3
            print(f" {num}%3 = {evn_rem}")
  else:
            print(num," -Odd number")
            odd_rem = num%2
            print(f" {num}%2 = {odd_rem}")


