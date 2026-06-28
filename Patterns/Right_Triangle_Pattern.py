"""
Write a Python program to print the following right triangle pattern.

*
**
***
****
*****
"""

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()
