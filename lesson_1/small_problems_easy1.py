# 1. Write a program that solicits six (6) numbers from the user and prints a
# message that describes whether the sixth number appears among the first five.

def numbers():
    nums = ['1st', '2nd', '3rd', '4th', '5th', '6th']
    num_list = list()
    for item in nums:
        num = int(input(f'Enter the {item} number: \n'))
        num_list.append(num)
    final = num_list.pop()
    if final in num_list:
        num_list = str(num_list)
        num_list = num_list[1:-1]
        print(f'{final} is in {num_list}')
    else:
        num_list = str(num_list)
        num_list = num_list[1:-1]
        print(f'{final} isn\'t in {num_list}')

# OR

# numbers = []

# numbers.append(input("Enter the 1st number: "))
# numbers.append(input("Enter the 2nd number: "))
# numbers.append(input("Enter the 3rd number: "))
# numbers.append(input("Enter the 4th number: "))
# numbers.append(input("Enter the 5th number: "))
# last_number = input("Enter the last number: ")
#
# numbers_list = ','.join(numbers)
# print(type(numbers_list))
# if last_number in numbers:
#     print(f"{last_number} is in {numbers_list}.")
# else:
#     print(f"{last_number} isn't in {numbers_list}.")



# Write a function that returns True if the string passed as an argument is
# a palindrome, False otherwise. A palindrome reads the same forwards and
# backwards. For this problem, the case matters and all characters matter.

def is_palindrome(string):
    return string == string[::-1]
# All of these examples should print True
print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)
print(is_palindrome('Madam') == False)
print(is_palindrome("madam i'm adam") == False)

# This time your function should be case-insensitive, and should ignore all
# non-alphanumeric characters

def is_real_palindrome(string):
    if string.isalnum():
        return string.casefold() == string.casefold()[::-1]
    else:
        new_string = ''
        for char in string:
            if char.isalnum():
                new_string += char
        return new_string.casefold() == new_string.casefold()[::-1]


print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True
print(is_real_palindrome('Madam') == True)           # True
print(is_real_palindrome("Madam, I'm Adam") == True) # True

# Write a function that takes a list of numbers and returns a list with
# the same number of elements, but with each element's value being the
# running total from the original list

def running_total(nums_list):
    if nums_list == []:
        return []
    total = [nums_list[0]]
    count = 0
    while count < len(nums_list) - 1:
        new_num = total[count] + nums_list[count + 1]
        total.append(new_num)
        count += 1
    return total

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

# OR
# def running_total(nums):
#     result_list = []
#     total = 0
#
#     for num in nums:
#         total += num
#         result_list.append(total)
#
#     return result_list


# Write a function that takes a string consisting of zero or more
# space-separated words and returns a dictionary that shows the number of
# words of different sizes. All of the examples should print True

def word_sizes(string):
    dict = {}
    lst = string.split()
    for word in lst:
        length = len(word)
        if length not in dict:
            dict[length] = 0
        dict[length] += 1
    return dict

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

# Now exclude non-letters

def word_sizes(string):
    new_string = ''
    for letter in string:
        if letter.isalpha() or letter == ' ':
            new_string += letter

    dict = {}
    lst = new_string.split()
    for word in lst:
        length = len(word)
        if length not in dict:
            dict[length] = 0
        dict[length] += 1
    return dict

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

# Given a string of words separated by spaces, write a function that swaps
# the first and last letters of every word. You may assume that every word
# contains at least one letter, and that the string will always contain at
# least one word. You may also assume that each string contains nothing but
# words and spaces, and that there are no leading, trailing, or repeated
# spaces.

def swap(string):
    lst = string.split()
    new_list = []
    for word in lst:
        if len(word) > 1:
            first = word[0]
            last = word[-1]
            middle = word[1:-1]
            new_word = last + middle + first
            new_list.append(new_word)
        else:
            new_list.append(word)
    result = ' '.join(new_list)
    return result

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

# OR

# def swap(words):
#     words_list = words.split()
#
#     for idx in range(len(words_list)):
#         words_list[idx] = swap_first_last_characters(words_list[idx])
#
#     return ' '.join(words_list)
#
# def swap_first_last_characters(word):
#     if len(word) == 1:
#         return word
#
#     return word[-1] + word[1:-1] + word[0]

# Write a function that takes a string of digits and returns the appropriate
# number as an integer. You may not use any of the standard conversion
# functions available in Python, such as int. Your function should calculate
# the result by using the characters in the string.

def string_to_integer(string):
    numbers = '0123456789'
    length = len(string) - 1
    counter = 0
    total = 0
    for item in string:
        for num in numbers:
            if item == num:
                total += counter * 10 ** length
                counter = 0
                length -= 1
                break
            counter += 1
    return total

print(string_to_integer("7321") == 7321)  # True
print(string_to_integer("570") == 570)    # True
print(string_to_integer("5709970") == 5709970)    # True
print(string_to_integer("0") == 0)    # True

# Their solution...yikes this was a tricky one
# def string_to_integer(s):
#     DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
#         '8': 8, '9': 9,}
#     value = 0
#     for char in s:
#         value = (10 * value) + DIGITS[char]
#     return value

def string_to_signed_integer(string):
    if string[0] != '-':
        if string[0] == '+':
            string = string[1:]
        result = string_to_integer(string)
    else:
        string = string[1:]
        result = -(string_to_integer(string))
    return result

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

# def string_to_signed_integer(string):
#     match string[0]:
#         case '-':
#             return -string_to_integer(string[1:])
#         case '+':
#             return string_to_integer(string[1:])
#         case _:
#             return string_to_integer(string)


# UNABLE TO DO THIS, SO NEED TO RETURN!!!!!!!!!!!!!!!!!!!!!!
# In the previous two exercises, you developed functions that convert simple
# numeric strings to signed integers. In this exercise and the next, you're
# going to reverse those functions. Write a function that converts a
# non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string
# representation of that integer.You may not use any of the standard
# conversion functions available in Python, such as str. Your function
# should do this the old-fashioned way and construct the string by analyzing
# and manipulating the number.

def integer_to_string(integer):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    result = ''
    while integer > 0:
        integer, index = divmod(integer, 10)
        result = numbers[index] + result
    return result or '0'

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

def signed_integer_to_string(number):
    if number == 0:
        result = integer_to_string(number)
    elif number < 0:
        number *= -1
        result = '-' + integer_to_string(number)
    else:
        result = '+' + integer_to_string(number)
    return result

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True


def dms(num):
    num = float(num)
    DEGREE = "\u00B0"
    total = ''
    splited = str(num).split('.')
    print(splited)
    degrees = splited[0]
    minute_string = '.' + splited[1]
    print(minute_string)
    minutes = float(minute_string) * 60
    minutes = str(minutes).split('.')
    seconds = minutes[1]
    seconds = '.' + seconds
    minutes = minutes[0]
    if len(minutes) == 1:
        minutes = '0' + minutes
    seconds = float(seconds) * 60
    seconds = str(int(seconds))
    quote = '"'
    if len(seconds) == 1:
        seconds = '0' + seconds
    total = degrees + DEGREE + minutes + "'" + seconds + quote
    return total