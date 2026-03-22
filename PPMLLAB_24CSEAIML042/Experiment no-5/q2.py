#WAP that loops over a sequence of elements of a list, tuple, dictionary and set
lst=[1,2,3]
tup=(4,5,6)
dic={1:'a',2:'b'}
st={7,8,9}
print("List:")
for i in lst:
    print(i)
print("Tuple:")
for i in tup:
    print(i)
print("Dictionary:")
for i in dic:
    print(i, dic[i])
print("Set:")
for i in st:
    print(i)