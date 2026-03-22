#wap to input your marks for three subjects then find sum and percentage
mark1=float(input("Subject 1 mark:"))
mark2=float(input("Subject 2 mark:"))
mark3=float(input("Subject 3 mark:"))
sum=mark1+mark2+mark3
percentage=(sum/300)*100
print("Sum:",sum)
print("Percentage:",percentage)