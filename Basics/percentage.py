# Write a Python program to calculate the percentage of five subjects.


english = float(input("Enter English Marks: "))
math = float(input("Enter Mathematics Marks: "))
science = float(input("Enter Science Marks: "))
computer = float(input("Enter Computer Marks: "))
hindi = float(input("Enter Hindi Marks: "))

total = english + math + science + computer + hindi
percentage = total / 5

print("Total Marks =", total)
print("Percentage =", percentage, "%")
