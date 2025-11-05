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


# Given an unordered list and the information that exactly one value in the
# list occurs twice (every other value occurs exactly once), determine which
# value occurs twice. Write a function that finds and returns the duplicate
# value. You may assume that the input list will always have exactly one
# duplicate value.

def find_dup(lst):
    for num in lst:
        count = lst.count(num)
        if count == 2:
            return num

print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True

# Write a function that combines two lists passed as arguments and returns a
# new list that contains all elements from both list arguments, with each
# element taken in alternation. You may assume that both input lists are
# non-empty, and that they have the same number of elements.
def interleave(lst1, lst2):
    final = []
    combined = zip(lst1, lst2)
    for item in combined:
        final.append(item[0])
        final.append(item[1])
    return final
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)

# Write a function that takes a list of positive integers as input,
# multiplies all of the integers together, divides the result by the number
# of entries in the list, and returns the result as a string with the value
# rounded to three decimal places.

def multiplicative_average(a_list):
    total = 1
    for num in a_list:
        total *= num
    avg = round(total/len(a_list), 3)
    avg_str = str(avg)
    avg = avg_str.split('.')
    end = avg[1]
    while len(end) < 3:
        end = end + '0'
    average = avg[0] + '.' + end
    return average

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")


# Write a function that takes two list arguments, each containing a list of
# numbers, and returns a new list that contains the product of each pair of
# numbers from the arguments that have the same index. You may assume that
# the arguments contain the same number of elements.

def multiply_list(lst1, lst2):
    zipped = zip(list1, list2)
    tups = [*zipped]
    total = [item[0] * item[1] for item in tups]
    return total

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

# Write a function that takes one argument, a positive integer, and returns a
# list of the digits in the number.

def digit_list(number):
    lst = [char for char in str(number)]
    nums = [int(char) for char in lst]
    return nums

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True


# Write a function that counts the number of occurrences of each element in a
# given list. Once counted, print each element alongside the number of
# occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").

def count_occurrences(a_list):
    dictionary = {}
    for item in a_list:
        dictionary.setdefault(item, 0)
        dictionary[item] += 1
    for key, value in dictionary.items():
        print(key, '=>',value)

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# Expected outcome
# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2