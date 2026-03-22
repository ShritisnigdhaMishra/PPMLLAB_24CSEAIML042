#WAP to print Fibonacci series upto n terms.
n=int(input("Enter n:"))
a=0
b=1
i=0
while(i<n):
    print(a,end = " ")
    a,b=b,a+b
    i=i+1