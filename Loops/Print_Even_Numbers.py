# Write a Python program to print all even numbers from 1 to N. 


n = int(input("Enter the value of N: "))

print("Even Numbers:")

for i in range(2, n + 1, 2):
    print(i)
