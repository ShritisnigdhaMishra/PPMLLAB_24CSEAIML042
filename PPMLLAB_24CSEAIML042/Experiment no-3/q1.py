#wap to test a string is palindrome or not
s=input("Enter a string:")
r=s[::-1]
if(s==r):
    print("The string is palindrome")
else :
    print("The stringis not palindrome")