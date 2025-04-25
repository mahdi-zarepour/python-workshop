"""
Manipulate List

List methods apply in-place because lists are mutable objects, 
i.e. the list itself is modified
----------
add items:
    - append(object):
        Adds an element at the end of the list
    - insert(index, object):
        Adds an element at the specified position
    - extend(iterable):
        Returns the number of elements with the specified value
read items:
    - index(value, start=0, stop=sys.maxsize):
        Returns the index of the first element with the specified value
    - reverse():
        Reverses the order of the list
    - sort(*, key, reverse):
        Sorts the list
delete items:
    - pop():
        Removes the element at the specified position or remove last item
    - remove():
        Removes the first item with the specified value
    - clear():
        Removes all the elements from the list
"""

# append(object: str, /) -> None
# names = ['Mahdi', 'Ali', 'Amir', 'Reze', 'Ali']
# names.append('Hamid')
# print(names)

# a = names.append('Yaghoub')
# print(a)

# insert(index: SupportsIndex, object: str, /) -> None
# names.insert(3, 'Hasan')
# print(names)

# names.insert(10, 'Akbar') # insert an element at the end of the list
# names.insert(-10, 'Akbar') # insert an element at the first of the list
# print(names)

# extend(iterable: Iterable[str]) -> None
# ages = [12, 22, 34, 11]
# ages.extend([78, 45])
# print(ages)

# The difference between methods append and extend
# ages.append(37, 43) # TypeError: list.append() takes exactly one argument (2 given)
# ages.append([37, 43])
# print(ages)

# ages.extend([16, [99, 23]])
# print(ages)


# --------------

# index(value, start=0, stop=sys.maxsize) -> int
# lessons = ['Mathematics', 'Statistics', 'Physics', 'Statistics']
# statistics_index = lessons.index('Statistics', 2)
# print(lessons)
# print(statistics_index)

# It does not count the last index
# statistics_index = lessons.index('Statistics', 20) # ValueError

# statistics_index = lessons.index('Physics', 0, 2) # ValueError


# reverse() -> None
# numbers = [1, 2, 3, 4, 5]
# a = numbers.reverse()
# print(numbers)

# b = numbers.reverse()
# print(b)
# print(numbers)


# sort(*, key: None = None, reverse: bool = False) -> None
# random_number = [-21, 3, -9, 19, -33, 43, 11]
# random_number.sort() # according  order.
# print(random_number)

# random_number = [-21, 3, -9, 19, -33, 43, 11]
# random_number.sort(reverse=True) # descending order.
# print(random_number)


# --------------

# pop(index: SupportsIndex = -1, /) -> str
# cities = ['Shiraz', 'Fasa', 'Darab']
# last = cities.pop()
# print(last)
# last = cities.pop(20) # IndexError: pop index out of range
# print(cities)
# print(last)

# cities.extend(['Lar', 'Jahrom'])
# first = cities.pop(0)
# print(cities)
# print(first)

# Reconstruction of the list of cities
# cities.extend(['Shiraz', 'Darab', 'Lar'])
# print(cities)

# remove(value: str, /) -> None
# cities.remove('Lar')
# cities.remove('Lare') # ValueError: list.remove(x): x not in list
# print(cities)


# clear() -> None
# print(cities)
# cities.clear()
# print(cities)

# delete list
# del cities[:]
# print(cities) # NameError: name 'cities' is not defined
