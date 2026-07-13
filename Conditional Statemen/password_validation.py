a = input("Enter password : ")
n = len(a) - 1
if((a[0] >= 'A' and a[0] <= 'z') and a[n] >= 'a' and a[n] <= 'z'):
     print("You choose strong password")
else:
  print("choose better one")

