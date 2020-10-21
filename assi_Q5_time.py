#Greet the user good morning, good evening, good afternoon depending on the time of the day inside variable hrs input from the user in 24hrs format.


time=float(input("Enter Time:--"))
 
if(time<12):
    print("Good Morning.......!")
elif(time<17):
    print("Good Afternoon.......!!")
elif(time<21):
    print("Good Evening......!!!")
else:
    print("Good Night......!!!!!")
      
    
