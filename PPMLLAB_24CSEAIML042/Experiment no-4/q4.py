#WAP to find the sum of digits of a positive integer.
n=int(input("Number:"))
Sum=0
while(n>0):
    temp=n%10
    Sum=Sum+temp
    n=n//10
print ("Sum of digits:", Sum)