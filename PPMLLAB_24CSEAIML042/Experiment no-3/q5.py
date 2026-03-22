#wap to input marks for 5 subjects[assume maximum marks for each subject is 50].find the percentage and then display grade as below:
#percentage>=90 and <=100 grade is O
#percentage>=80 and <90 grade is E
#percentage>=70 and <80 grade is A
#percentage>=60 and <70 grade is B
#percentage>=50 and <60 grade is C
#percentage>=0 and <50 grade is F
m1=float(input("Subject 1 mark:"))
m2=float(input("Subject 2 mark:"))
m3=float(input("Subject 3 mark:"))
m4=float(input("Subject 4 mark:"))
m5=float(input("Subject 5 mark:"))
percentage = ((m1+m2+m3+m4+m5)/250)*100
print("Percentage:",percentage)
if(percentage >= 90 and percentage <= 100):
    print("Grade is O")
elif(percentage >= 80 and percentage < 90):
    print("Grade is E")
elif(percentage >= 70 and percentage < 80):
    print("Grade is A")
elif(percentage >= 60 and percentage < 70):
    print("Grade is B")
elif(percentage >= 50 and percentage < 60):
    print("Grade is C")
elif(percentage >= 0 and percentage < 50):
    print("Grade is F")
else:
    print("Invalid marks")