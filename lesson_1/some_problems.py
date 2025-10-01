def calculate_leftover_blocks(number):
    result = 0
    count = 1
    while number > 0:
        number = number - count**2
        count += 1
        if count**2 > number:
            result = number
            break
    return result

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
print(calculate_leftover_blocks(199) == 59) # True
print(calculate_leftover_blocks(15) == 1) # True

def select_fruit(dictionary):
    only_fruits = {}
    for key, value in dictionary.items():
        if value == 'Fruit':
            only_fruits[key] = value
    return only_fruits

produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }