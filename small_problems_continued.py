# Write a function that takes two lists as arguments and returns a set that
# contains the union of the values from the two lists. You may assume that
# both arguments will always be lists.

def union(lst1, lst2):
    total = set(lst1) | set(lst2)
    return total

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

# Write a function that takes a list as an argument and returns a list that
# contains two elements, both of which are lists. Put the first half of the
# original list elements in the first element of the return value and put
# the second half in the second element. If the original list contains an
# odd number of elements, place the middle element in the first half list

def halvsies(lst):
    length = len(lst)
    half = length // 2
    if length == 1:
        first = lst[:]
        second = []
    elif length % 2 == 0:
        first = lst[:half]
        second = lst[2:]
    else:
        first = lst[:half + 1]
        second = lst[half + 1:]
    return [first, second]