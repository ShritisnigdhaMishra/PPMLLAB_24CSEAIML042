#Write a function to check whether a number is even or odd.
def check(a):
    if(a%2==0):
        return "even"
    else:
        return "odd"
a=int(input("Number:"))
print(a,"is",check(a))