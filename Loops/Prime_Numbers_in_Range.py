# Write a Python program to print all prime numbers from 1 to N.


n = int(input("Enter N: "))

print("Prime Numbers:")

for num in range(2, n + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
