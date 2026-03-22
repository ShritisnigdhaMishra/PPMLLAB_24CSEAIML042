#Find the minimum element in a list
def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    return min(lst[0], find_min(lst[1:]))
numbers = [5, 2, 9, 1, 7]
print(find_min(numbers))