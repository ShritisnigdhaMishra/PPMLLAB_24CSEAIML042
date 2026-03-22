#WAP to input a sentence, store each word as element into a list LIST1. Now display the element of list along with its index (using enumerate()). Create another list LIST2 having elements as a series of numbers. Now use zip() to combine the elements of both lists to create a 3rd list LIST3 and then display it.
i=input("Sentence:")
LIST1=i.split()
print("\nElements of LIST1 with index:")
for i,w in enumerate(LIST1):
    print(i,w)
LIST2=list(range(1,len(LIST1)+1))
LIST3=list(zip(LIST1,LIST2))
print("\nCombined LIST3 using zip:")
print(LIST3)