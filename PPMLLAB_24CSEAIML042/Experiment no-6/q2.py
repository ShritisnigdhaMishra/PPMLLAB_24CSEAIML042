#WAP to create a dictionary and input keys, and values, then create another dictionary which collects the values of 1st dictionary as key and key of 1st dictionary as values and then display both dictionaries.
d={}
n=int(input("No of key value pairs:"))
for i in range(n):
    k=input("key:")
    v=input("value:")
    d[k]=v
rev={}
for k,v in d.items():
    rev[v]=k
print("\nOriginal dictionary:")
print(d)
print("\nReversed dictionary:")
print(rev)