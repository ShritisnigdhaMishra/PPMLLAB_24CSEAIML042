#wap to find the area and perimeter of a triangle 
a=5
b=3
c=4
perimeter=a+b+c
s=perimeter/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area:",area)
print("Perimeter:",perimeter)