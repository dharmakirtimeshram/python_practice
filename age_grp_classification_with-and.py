"""
Age Group Classification with AND:
Create a python program to classify a person's age group. Classify them as a child (less than 13),
teenager (between 13 and 19), and an adult (20 and above) using both logical AND and OR.
Sample Data:
Age: 15

"""
age = int(input("Enter age :- "))
if age >= 20:
    print("This person is in an adult group")
elif age>=13 and age<=19:
    print("This person is in teenager group")
elif age < 13:
    print("This person is in child group")