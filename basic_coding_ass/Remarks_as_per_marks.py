'''
Check whether the number is in range 0-100 or not.
 If not in range print invalid input.
 Else – if the number is in range
 90-100 then print Super Smart,
 80-90 print Smart,
 70-80 print smart enough,
 60-70 print just smart,
 35-60 print no smart,
 0-35 print dump.

'''

user_in = int(input("Enter your Number - "))

if(user_in > 0 | user_in <= 100):
    print("Invalid input")

else:
     if(user_in>90):
            print("Super smart")

     elif(user_in>80 and user_in<=90):
            print(" Smart")

     elif(user_in>70 and user_in<=80):
            print("smart enough")

     elif(user_in>60 and user_in<=70):
            print("Just smart")

     elif(user_in>=35 and user_in<=60):
            print("No smart")

     else:
            print("Dump")