a = int(input("Enter year :"))
if(a  % 100 != 0 and a % 4 == 0 and a % 400 ):
    print("leap year")
else:
    print("this year is not leap year")
