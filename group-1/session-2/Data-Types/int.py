"""
Integer data type

How to deal with integer numbers in Python
"""

# somebody info!
score = -12
age = 32
height = 170
salary = 80_000

print(score, age, height, salary, sep=' | ',)

# int class (function-style name)
zero = int()
int_num = int(29)
convert_to_int = int(50.223)

print(zero, int_num, convert_to_int, sep=' -- ')

# type()
print('age type: ', type(age))
print('int() type:', type(zero))
print('type of 50.223: ', type(50.223))
print('convert_to_int type:', type(zero))
