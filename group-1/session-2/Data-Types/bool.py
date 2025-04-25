"""
Boolean data type

How to deal with Boolean algebra in Python
"""

t = True
f = False

print(t, f, sep=' | ')
print(type(t), type(f), sep=' --- ')

# the bool type is a subclass of int
print('the bool is a subclass of int?', issubclass(bool, int))
print(True + True + True)

# bool class (function-style name)
print('name: ', bool('Mahdi'))
print('None:', bool(None))
print('Zero:', bool(0.0))
print('empty string: ', bool(''))
print('empty list: ', bool([]))
