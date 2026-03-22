#wap to find the greatest among three unequal numbers
x=int(input("First number:"))
y=int(input("Second number:"))
z=int(input("Third number:"))
if(x>y and x>z):
    print(f"{x} is the greatest")
elif(y>z):
    print(f"{y} is the greatest")
else:
    print(f"{z} is the greatest")