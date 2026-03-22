#Write a function to find the factorial of a number.
def fact(a):
    if(a==1):
        return 1
    else:
        return a*fact(a-1)
a=int(input("Number:"))
print("Factorial is:",fact(a))