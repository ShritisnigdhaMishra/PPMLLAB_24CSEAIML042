#WAP to create a string which contains a paragraph. Now find
#i) Count how many words it contains
#ii) How many palindrome exist
#iii) Print each word in reverse order.
s=input("Paragraph:")
l=s.split()
print("This paragraph contains",len(l),"words")
count=0
for i in l:
    if(i==i[::-1]):
        count +=1
print("Palindrome exists:",count)
print("Words in reversed order:")
for i in l:
    print(i[::-1])