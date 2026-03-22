#WAP to create a list which contains some group of fruit names. Display the elements of list from last index to 1st index (reversely) and also show the length of each element. Create another list which collects the reverse of each element.
l=["Apple","Banana","Mango"]
print("Length of each element:")
for i in l[::-1]:
    print(i,"length is",len(i))
print("\nList containing reverse of each fruit name:")
rev =[]
for fruit in l:
    rev.append(fruit[::-1])
print(rev)