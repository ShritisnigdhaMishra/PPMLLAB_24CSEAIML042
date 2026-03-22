#Write a function to calculate simple interest.
def si(p,r,t):
    return (p*r*t)/100
p=float(input("Principal amount:"))
r=float(input("Rate of interest:"))
t=float(input("Time in years:"))
print("Simple interest:",si(p,r,t))