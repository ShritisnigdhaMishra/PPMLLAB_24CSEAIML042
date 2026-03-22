#WAP to find factorial of a number.
n=int(input("Number:"))
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print("factorial:",fact)