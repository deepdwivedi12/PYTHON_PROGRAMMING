# Write a Python program to print the multiplication table of a number.


num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
