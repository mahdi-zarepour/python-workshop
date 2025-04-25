"""
Data Structure (list)

List
----------
create:
    - List literals:
        They consist of a pair of square brackets enclosing a
        comma-separated series of objects. Note that you don't
        have to declare the items' type or the list's size beforehand.
    - list() constructor:
        You can call this constructor with any iterable object,
        including other lists, tuples, sets, dictionaries and
        their components, strings, and many others.
        You can also call it without any arguments,
        in which case you'll get an empty list back.
    - List comprehension:
        List comprehensions allow you to quickly create and transform lists
        using a syntax that mimics a for loop but in a single line of code.
        [expression(item) for item in iterable if <expr>]
        [expression(item) if <expr> else <statement> for item in iterable]
read:
    - indexing:
        Indexing your list with different indices gives you direct access
        to the underlying items
    - slicing:
        list[start:stop:step]
update:
    Python lists are mutable data types. This means that you can change their
    elements without changing the identity of the underlying list.
    - Index assignment
    - Slicing assignment
"""

# list()
list_method = list(
    (1, 2, 3)
)
# print(list_method)

empty_list = list()
# print(id(empty_list))
# print(empty_list)

names: list = ['Mahdi', 'Reza', 'Hamid', 'Fatemeh', 'Zahra', 'Mona']
# print(names)

info: list = ['Narges Taherie', 36, 168.2, 70.6] # full name, age, height, weight
# print(info)
# print('full name:', info[0], 'age:', info[1], sep='\n')
# print(info[5]) # IndexError: list index out of range

# full name, age
users: list = [
    ['Mahdi Zarepour', 20],
    ['Reza Ghaderie', 32],
    ['Mona Mohammadi', 29],
    ['Zahra Taghavie', 17],
]
# print(users)
# print('full name:', users[0][0], 'age:', users[0][1])

# indexError
# print(users[10])
# print(users[1][3])

company_name = list('Google')
# print(company_name)
# print(company_name[0:5:3])
# print(company_name[:])
# print(company_name[::])
# print(company_name[10:])
# print(company_name[:10])
# print(company_name[-6:-1])

# len()
# print(len(names), len(users))

# List comprehension
power: list = [x ** 2 for x in range(11)]   
# print(power)

even_number: list = [x for x in range(11) if x % 2 == 0]
# print(even_number)

even_number_or_None: list = [x ** 2 if x % 2 == 0 else None for x in range(11)]
# print(even_number_or_None)

# Update list
cities = ['Shiraz', 'Tehran', 'Kerman', 'Yazd']
# print(id(cities))

# index assignment
# cities[1] = 'Tabriz'
# print(id(cities))

# cities[-1] = 'Bandar Abbas'
# cities[0] = ['Birjand', 'Hamedan']
# print(cities, id(cities), sep='\n')

# slicing assignment
cities = ['Shiraz', 'Tehran', 'Kerman', 'Yazd']
# cities[0:2] = ['Rasht', 'Gorgan']
# cities[0:1] = ['Rasht', 'Gorgan']
# cities[0:3] = ['Rasht', 'Gorgan']
# cities[1:] = ['Mashhad', 'Esfahan', 'Zahedan']
# cities[2:] = ['Mashhad', 'Esfahan', 'Zahedan']
# print(cities)

numbers = [1, 2, 0, 0, 0, 0, 5, 6, 7]
numbers[2:6] = [3, 4]
# print(numbers)
