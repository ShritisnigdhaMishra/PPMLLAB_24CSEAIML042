#Palindrome using recursive function.
def palindrome(s):
    if s == "":
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])
word = input("Enter a word:")
if palindrome(word):
    print("palindrome")
else:
    print("Not palindrome")