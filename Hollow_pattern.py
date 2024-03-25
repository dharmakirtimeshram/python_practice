"""
HOLLOW PATTERN
* * * * * *
* *
* *
* * * * * *
"""

for i in range(6, 1, -4):
    for j in range(1, i+1):
        print("* ", end="")
    print()
for m in range(2, 7, 4):
    for n in range(1, m+1):
        print("* ",end="")
    print()