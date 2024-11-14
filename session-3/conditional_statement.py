"""
Conditional Statement

Operator
----------
if <expr>:
    <statement>
elif <expr>:
    <statement>
else:
    <statement>
"""

# age = float(input('Enter your age: '))

# if (age > 18): # <expr>
#     print('You are adult') # <statement>

# if age > 18: # <expr>
#     print('You are adult') # <statement>
# else:
#     print('You are under the legal age') # <statement>


# score = float(input('Enter your math score: '))

# if score < 10:
#     print('Fail')
# elif (score > 10) and (score < 15):
#     print('You are good student')
# else:
#     print('You are great!')


# first_name = input('Enter your first name: ')
# last_name = input('Enter your last name: ')

names = [
    'Mahdi', 'Ali', 'Fatemeh', 'Zahra', 'Zare', 'Alavie', 'Hasanie'
]

# if (first_name in names) or (last_name in names):
#     first_name, last_name = first_name.capitalize(), last_name.capitalize()
#     print(first_name, last_name)
# else:
#     print('Who are you?')


# if 1:
#     print('1 is True')
# elif 1 / 0:
#     print('ZeroDivisionError: division by zero')
# else:
#     print(variable)

# if (y := input('Enter a letter: ')) == 'a':
#     pass
# else:
#     print(y)

# if x > 10:  print('gt 10'); x += 10; print(x)

# if (x := float(input('Enter a number: '))) > 10: print('gt 10'); x += 10; print(x)

# x = float(input('Enter a number: '))
# print('gt 10') if x > 10 else print('lt 10')

if 'هوا بارانی بود':
    if 'هوا سرد هم بود':
        print('A')

a = 'Mahdi'
if 'i' in a:
    print('i')

num = 25555
if 2 in num: print(2)