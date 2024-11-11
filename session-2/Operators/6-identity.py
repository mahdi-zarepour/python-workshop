"""
Identity Operators

Operator
----------
is :
    True if x and y hold a reference to the same in-memory object
is not :
    True if x points to an object different from the object that y points to
"""

num1 = 10
num2 = 10
# num2 = 10.0
print(id(num1), id(num2), sep='\n')
print('identity operator is:', num1 is num2)
print('equality operator == :', num1 == num2)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(id(list1), id(list2), sep='\n')
print('identity operator is:', list1 is list2)
print('equality operator == :', list1 == list2)
