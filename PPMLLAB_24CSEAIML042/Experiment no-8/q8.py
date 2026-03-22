#Write a function to find the largest of 3 numbers.
def largest(a,b,c):
    if(a>=b and a>=c):
        return a
    elif(b>=a and b>=c):
        return b
    else:
        return c
a=int(input("First no:"))
b=int(input("Second no:"))
c=int(input("Third no:"))
print("Largest no:",largest(a,b,c))