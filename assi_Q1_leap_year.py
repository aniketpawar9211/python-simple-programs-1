#Write a program to check if the given is year is leap year or not.

year=int(input("Enter year:----"))

if(year%4==0 and year%100!=0 or year%4==0 and year%400==0):
    print("Given Year {} is leap Year".format(year))
else:
    print("Given Year {} is not Leap year".format(year))
