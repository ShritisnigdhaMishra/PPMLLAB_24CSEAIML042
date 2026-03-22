#WAP to print sum of numbers in a list using reduce() function.
from functools import reduce
numbers = [1,2,3,4,5]
total = reduce(lambda x,y: x+y, numbers)
print("Sum:", total)