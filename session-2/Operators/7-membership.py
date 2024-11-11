"""
Membership Operators

Operator
----------
in :
    True if value is present in collection
not in :
    True if value is not present in collection of values
"""

names = ['Mahdi', 'Ali', 'Zahra', 'Sarah']

print('Zahra' in names)
print('Reza' in names)

sport = 'Football'
print('f' in sport)
print('H' not in sport)
# print(not 'H' in sport) # Don't use not object in sequence

# print(1 in True) # TypeError: argument of type 'bool' is not iterable
