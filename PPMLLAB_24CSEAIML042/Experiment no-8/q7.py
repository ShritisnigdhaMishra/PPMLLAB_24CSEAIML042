#Write a function to count vowels in a string.
def count(s):
    count=0
    for ch in s:
        if ch in "aeiouAEIOU":
            count +=1
    return count
s=input("String:")
print("No. of vowels:",count(s))