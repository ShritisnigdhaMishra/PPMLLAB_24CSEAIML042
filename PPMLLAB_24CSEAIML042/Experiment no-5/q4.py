#WAP to create an empty list and input a group of numbers into the list, remove the duplicate elements from it and then sort them in ascending order and then display.
lst=[]
n=int(input("Enter no. of elements:"))
for i in range(n):
    lst.append(int(input()))
lst=list(set(lst))
lst.sort()
print("Sorted list:",lst)