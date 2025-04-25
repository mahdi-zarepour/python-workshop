"""
Variable in Python
"""
import keyword


# assign variable
a = 1
b = 2
c = 3
name = 'Mahdi'
family = 'Zarepour'

# print('b -> ', a)
# print('b -> ', b)
# print('name -> ', name)
# print('family -> ', family)


# Many Values to Multiple Variables
car, motor, truck = 'BMW', 'Kawasaki', 'Volvo'
# h, a, m, i = 'hamid' # ValueError: too many values to unpack (expected 4)
# h, a, m, i, d, e = 'hamid' # ValueError: not enough values to unpack (expected 6, got 5)

# # One Value to Multiple Variables
x = y = z = 'math variables!!!'
reza = hasan =  ali = 21

# print(car)
# print('motor ->', motor)
# print('truck ->', truck)
# print(x, y, z, sep=', ')
# print(h, a, m, i, d, e)


# print('--- methods ---')

# # iskeyword method
# print('is if a keywords? ->', keyword.iskeyword('None'))
# print('is IF keywords? ->', keyword.iskeyword('IF'))

# # isidentifier method
# print('1name'.isidentifier())
# print('1_name'.isidentifier())
# print('full name'.isidentifier())
# print('full_name'.isidentifier()) # True
# print('None'.isidentifier()) # isidentifier doesn't check keywords
