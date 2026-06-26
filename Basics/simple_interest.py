# Write a Python program to calculate Simple Interest.


principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (Years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)
