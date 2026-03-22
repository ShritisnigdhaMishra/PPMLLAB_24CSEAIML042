#WAP to create a list containing natural numbers from m to n where m and n given input (create using for loop). find the sum, average, largest and smallest in the list. Create another list which contains all the members of 1st list except numbers divisible by 3
m=int(input("Starting of natural number:"))
n=int(input("Ending of natural number:"))
l=[x for x in range(m,n+1)]
print("Sum of list:",sum(l))
print("Average of list:",(sum(l)/len(l)))
print("Largest of list:",max(l))
print("Smallest of list:",min(l))
l2=[x for x in l if(x%3!=0)]
print("Element not divisible by 3:",l2)