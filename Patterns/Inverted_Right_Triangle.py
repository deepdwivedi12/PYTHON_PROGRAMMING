"""
Write a Python program to print the following inverted triangle.

*****
****
***
**
*
"""

rows = 5

for i in range(rows, 0, -1):
    print("*" * i)
