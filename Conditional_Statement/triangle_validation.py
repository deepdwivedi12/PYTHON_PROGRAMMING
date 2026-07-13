angle1 = int(input("Enter your age1 :"))
angle2 = int(input("Enter your age2 :"))
angle3 = int(input("Enter your age3 :"))
if((angle1  >= 0 and angle2 >= 0 and angle3 >= 0 ) and (angle1 + angle2 + angle3) == 180):
     print("this is a triangle")
else:
  print("this is not a triangle")
