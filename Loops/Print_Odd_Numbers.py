# Write a Python program to print all odd numbers from 1 to N.
  

n = int(input("Enter the value of N: "))

print("Odd Numbers:")

for i in range(1, n + 1, 2):
    print(i)
