# Write a Python program to find the sum of the first N natural numbers.


n = int(input("Enter the value of N: "))

sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum =", sum)
