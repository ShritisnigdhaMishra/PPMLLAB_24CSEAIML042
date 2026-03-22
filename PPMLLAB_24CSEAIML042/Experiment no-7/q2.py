#Write a program to generate all prime numbers within a given range from m to n.
m=int(input("Starting of natural number:"))
n=int(input("Ending of natural number:"))
print("Prime numbers:",end=" ")
for i in range(m,n+1):
    if(n>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i,end=" ")