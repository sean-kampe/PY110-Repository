tup_nums = (11, 32, 3, 66, -12, 5, 2)
new = sorted(tup_nums)  # returns a list
print(new)

# not mutating
lst = [10, 9, -6, 11, 7, -16, 50, 8]
lst_a = sorted(lst)
lst_b = sorted(lst, reverse = True)
print(lst_a, lst_b)

# mutating
lst.sort()
print(lst)
lst.sort(reverse =  True)
print(lst)

# now sort according to string values but return nums
lst = [10, 9, -6, 11, 7, -16, 50, 8]
lst = [str(i) for i in lst]
lst.sort()
lst = [int(i) for i in lst]

# Their solutions are much better
lst.sort(key=str)
# or
def to_str(x):
    return str(x)

lst.sort(key=to_str)

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]
def year(book):
    return int(book['published'])

books.sort(key=year)
print(books)

# Nested stuff
lst = [[1], [2]]

lst[0].append([9])
print(lst)                 # [[1, [9]], [2]]
print(lst[0][1][0])

lst = [{"a": "ant"}, {"b": "bear"}]
lst[0]['c'] = 'cat'
print(lst)

# For each object shown below, demonstrate how you would access the letter g
lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]
print(lst1[2][1][3])

lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]
print(lst2[1]['third'][0])

lst3 = [['abc'], ['def'], {'third': ['ghi']}]
print(lst3[2]['third'][0][0])

dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}
print(dict1['b'][1])

# This one is much more challenging than it looks! Try it, but don't
# stress about it. If you don't solve it in 10 minutes, you can look
# at the answer.
dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}
print(list(dict2['3rd'].keys())[0])

# Demonstrate how you would change the value 3 to 4
lst1 = [1, [2, 3], 4]
lst1[1][1] = 4
print(lst1)
lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]
lst2[2] = 4
print(lst2)
dict1 = {'first': [1, 2, [3]]}
dict1['first'][2][0] = 4
print(dict1)
dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}
dict2['a']['a'][2] = 4
print(dict2)


# COMPREHENSIONS

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for key, value in munsters.items():
    print(f"{key} is a {value['age']} year-old {value['gender']}")

# Compute and display the total age of the family's male members. Try
# working out the answer two ways: first with an ordinary loop, then with a
# comprehension ---> result should be 444

total = 0
for value in munsters.values():
    if value['gender'] == 'male':
        total += value['age']
print(total)

total = [munsters[i]['age'] for i in munsters if munsters[i]['gender'] ==
         'male']
total = sum(total)

# Their solution
# all_male_ages = [member['age'] for member in munsters.values()
#                                if member['gender'] == 'male']

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
new_lst = [sorted(item) for item in lst]
print(new_lst)
for item in lst:
    item.sort()
print(lst)

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]
dictionary = {sublist[0]: sublist[1] for sublist in lst}
print(dictionary)

# Even better
better = dict(lst)
print(better)

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def find_odd(sublist):
    total = [element for element in sublist if element % 2 != 0]
    return sum(total)

new_lst = sorted(lst, key = find_odd)
print(new_lst)





# VERY IMPORTANT TO STUDY THIS BELOW, HARD, GOOD LESSONS!


# Given the following data structure, return a new list identical in
# structure to the original but, with each number incremented by 1. Do not
# modify the original data structure. Use a comprehension.
lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
# Expected result
# [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

def increment_values(dictionary):
    return {key: value + 1 for key, value in dictionary.items()}

new_list = [increment_values(value) for value in lst]

print(new_list, lst, sep='\n')
# [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]
# [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# or
new_list = [{key: value + 1 for key, value in dictionary.items()}
                            for dictionary in lst]

# or my awful solution, but it works
def increment(dictionary):
    new = {}
    for key, value in dictionary.items():
        new.setdefault(key, value + 1)
    return new

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
new_list = [increment(item) for item in lst]
print(new_list)



# Given the following data structure return a new list identical in
# structure to the original, but containing only the numbers that are
# multiples of 3

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
def return_new(lst):
    return [i for i in lst if i % 3 == 0]
new_list = [return_new(item) for item in lst]

# Comprehenshions problem 8---------------------------

# Given the following data structure, write some code to return a list that
# contains the colors of the fruits and the sizes of the vegetables. The
# sizes should be uppercase, and the colors should be capitalized.

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def helper(item):
    new = item['colors']
    new = [color.capitalize() for color in new]
    if item['type'] == 'vegetable':
        new = ''
        new = item['size'].upper()
    return new

produce = [helper(dict1[i]) for i in dict1]
print(produce)


# problem 9. Write some code to return a list that contains only the
# dictionaries where all the numbers are even

def find_evens(dictionary):
    checker = True
    lists = list(dictionary.values())
    for item in lists:
        for num in item:
            if num % 2 != 0:
                checker = False
    if checker:
        return dictionary

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

only_even = [find_evens(item) for item in lst if find_evens(item) != None]

# 10
import random
def build_UUID():
    text = '0123456789abcdef'
    UUID = random.choices(text, k = 32)
    UUID = ''.join(UUID)
    UUID = UUID[:9] + "-" + UUID[9:13] + "-" + UUID[13:17] + "-" + UUID[
                                                                   17:21] + \
           "-" + \
           UUID[21:]
    return UUID
print(build_UUID())


# 11. The following dictionary has list values that contains strings. Write
# some code to create a list of every vowel (a, e, i, o, u) that appears in
# the contained strings, then print it.
dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

def extract_vowel(text):
    vowels = 'aeiou'
    string = ''
    for item in text:
        for word in item:
            for letter in word:
                if letter in vowels:
                    string += letter
    return string

def list_of_vowels(dictionary):
    lst = [pair for pair in extract_vowel(dictionary.values())]
    return lst

print(list_of_vowels(dict1))

vowels = 'aeiou'

chars = [char for key in dict1
              for word in dict1[key]
              for char in word if char in vowels]

print(chars)