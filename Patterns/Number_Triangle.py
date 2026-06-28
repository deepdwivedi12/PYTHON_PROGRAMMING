"""
Write a Python program to print the following number pattern.

1
12
123
1234
12345
"""

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
