#WAP to test a number is prime or not.
n=int(input("Enter a number:"))
i=2
while(i<n):
    if(n%i==0) :
        print (n, "is not a prime number")
        break
    i+=1
else:
    print(n," is a prime number")