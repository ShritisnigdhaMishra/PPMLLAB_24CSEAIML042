#wap to accept a digit within 0 to 6 and display the weekday such as:0 for Sunday,1 for Monday,etc 
x=int(input("Enter a digit:"))
if(x==0):
    print("Sunday")
elif(x==1):
    print("Monday")
elif(x==2):
    print("Tuesday")
elif(x==3):
    print("Wednesday")
elif(x==4):
    print("Thursday")
elif(x==5):
    print("Friday")
elif(x==6):
    print("Saturday")
else:
    print("Invalid digit")