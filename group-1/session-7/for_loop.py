"""
Collection-Based Loop

----------
syntax:
    for <var> in <iterable>:
        <statement(s)>
    else:
        <statement(s)>
"""

# for item in ['Mahdi', 'Reza', 'Fatemeh', 'Amir']:
#     print(item)

# TypeError: 'int' object is not iterable
# for item in 123:
#     print(item)

# names = ['Mahdi', 'Reza', 'Fatemeh', 'Amir']
# for item in names:
#     print(item)

# for loop with conditional statement
# numbers = [1, 2, 3, 4, 5, 6]
# for item in numbers:
#     if item % 2 == 0:
#         print(item, 'is even')
#     else:
#         print(item, 'is odd')

# pass statement
# for item in numbers:
#     if item % 2 == 0:
#         pass
#     else:
#         print(item, 'is odd')

# break statement
# for item in numbers:
#     if item == 4:
#         break
#     else:
#         print(item)

# for item in numbers:
#     if item % 2 == 0:
#         continue
#     else:
#         print(item, 'is odd')
    
#     print('Done')

# else statement
# for item in numbers:
#     if item % 2 == 0:
#         print(item, 'is even')
#     else:
#         print(item, 'is odd')

#     if item > 3:
#         break
# else:
#     print('Done ...')

# range function
# range_0_to_10 = range(0, 10)
# print(range_0_to_10, type(range_0_to_10), sep=', ')
# print(list(range_0_to_10))

# for item in range(0, 10, 1): print(item)
# print(ont_to_ten)

# ont_to_ten_even = [i ** 2 for i in range(10) if i % 2 == 0]
# print(ont_to_ten_even)


# Iterators
# ages = [12, 32, 89, 65]
# itr_age = iter(ages)
# print(type(itr_age))
# print(next(itr_age))
# print(next(itr_age))
# print(next(itr_age))
# print(next(itr_age))
# print(next(itr_age))

# def upper(string):
#     return string.upper()

# def foreach(iterable, function):
#     itr = iter(iterable)
#     while True:
#         try:
#             i = next(itr)
#             print(function(i))
#         except StopIteration:
#             break

# foreach('fatemeh', upper)
