# Write a Python program to check whether a string is a palindrome.

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome String")
else:
    print("Not a Palindrome String")
