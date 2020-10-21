#Calculate the bmi using the formula wt / ht^2 and categorize the bmi as underweight if it is less than 18, normal between 18 to 22.5 and overweight till 25 while obese for 25 and above.


wt=float(input("Enter Wight:--"))
ht=float(input("Enter Hight:--"))

bmi=wt/ht*ht

print("Body Mass Index is {}".format(bmi))
