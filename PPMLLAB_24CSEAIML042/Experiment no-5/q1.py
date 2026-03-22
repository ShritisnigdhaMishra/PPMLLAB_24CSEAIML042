#Generate Fibonacci series between 0 to 1000, then find the Sum of even valued terms.
a=0
b=1
Sum=0
print ("Fibonacci series:")
for i in range(1000):
    if(a>1000):
        break
    print(a,end=" ")
    if(a%2==0):
        Sum=Sum+a
    c=a+b
    a=b
    b=c
print ("\nSum of even valued terms:",Sum)