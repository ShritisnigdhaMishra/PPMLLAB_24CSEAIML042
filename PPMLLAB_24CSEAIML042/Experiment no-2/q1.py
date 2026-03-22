#wap to display simple interest and compound interest
p=float(input("Principal amount:"))
r=float(input("Rate of interest:"))
t=float(input("Time in years:"))
n=int(input("Number of times interest compounded per year:"))
si=(p*r*t)/100
a=p*(1+(r/(100*n)))**(n*t)
ci=a-p
print("Simple interest:",si)
print("Compound interest:",ci)