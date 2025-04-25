"""
Float data type

How to deal with float numebrs in Python
"""

pi = 3.14
sqrt2 = 1.414
depth = -0.0001
division = 10 / 2

print(pi, sqrt2, depth, division, sep=' | ')

# float class (function-style name)
f0 = float()
convert_to_float = float(11)

print(f0, convert_to_float, sep=' -- ')

print('pi type:', type(pi))
print('division type: ', type(division))
print('convert_to_float type:', type(convert_to_float))
