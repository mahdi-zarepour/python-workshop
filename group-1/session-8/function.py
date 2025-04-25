"""
Function

----------
syntax:
    def <function_name>([<parameters>]):
        <statement(s)>

function calls and definition

argument passing:
    - positional arguments:
        - The most straightforward way to pass arguments to a Python function
          is with positional arguments (also called required arguments).

    - keyword arguments:
        - When you’re calling a function, you can specify arguments in the form
         <keyword>=<value>. In that case, each <keyword> must match a parameter
         in the Python function definition.

    - default parameters:
        - If a parameter specified in a Python function definition has the form
          <name>=<value>, then <value> becomes a default value for that parameter.
          Parameters defined this way are referred to as
          default or optional parameters

mutable default parameter values:
    In Python, default parameter values are defined only once when the
    function is defined (that is, when the def statement is executed).
    The default value isn’t re-defined each time the function is called.

return statement:
    - return terminates the function
    - pass data back to the caller
    - return special value None for use in conditional statements
"""

import math


# --------- built in function ---------

# ages = [21, 22, 32, 87, 45, 12]

# ages.sort()
# print(ages)

# ages.reverse()
# print(ages)

# index_0 = ages.pop(-1)
# print(index_0)
# print(ages)


# full_name = 'mahdi,zarepour'

# full_name = full_name.replace(',', ' ')
# print(full_name)

# full_name = full_name.title()
# print(full_name)


# --------- function definition ---------


# def say_hello():
#     print('Hello !!!')

# say_hello()

# def say_goodbye():
#     print('Goodbye ...')

# say_goodbye()


# --------- Positional arguments ---------


# Positional arguments or Required arguments
# def f(x):
#     print(x)

# f(4)


# def car_price(car_name, price):
#     print(car_name, 'cost', price)

# car_price('Pride', 0)
# car_price(1000, 'Cerato')
# car_price(1000, 'Cerato') # Arguments order
# car_price('Cerato') # TypeError: missing 1 "required positional argument"
# car_price('Cerato', 1000, 'HA HA HA') # TypeError: takes 2 "positional arguments" but 3 were given


# --------- Keyword arguments ---------


# Keyword arguments: lifts the restriction on argument order but 
# the number of arguments and parameters must still match


# def full_name(first_name, last_name, age):
#     print(first_name, last_name, age)


# full_name(last_name='Zarepour', first_name='Mahdi')
# full_name('Mahdi', age=22, last_name='Zarepour')
# full_name(last_name='Hamidi', first_name='Farzaneh') # Handle arguments order
# full_name(first_name='Fatemeh') # TypeError: missing 1 required positional argument: 'last_name'
# full_name(first_name='Reza', last_name='Akbari', age=22, email='vsfs') # TypeError: got an unexpected keyword argument 'age'


# def user_info(first_name, last_name, age, email):
#     print(first_name, last_name, 'is', age, 'years old')

# user_info('Hashem', last_name='Salarie', 23, email='HS@gmail.com') # SyntaxError: positional argument follows keyword argument
# user_info('Hashem', 'Salarie', age=23, email='HS@gmail.com')


# --------- default parameters ---------


# def power(x, p=2):
#     print(x ** p)

# power(2)
# power(2, p=5)

# def addition(a=1, b): # SyntaxError: parameter without a default follows parameter with a default
#     print(a + b)

# addition(9, 20)


# --------- mutable default parameter values ---------


# def names_list(names=[]):
#     print(id(names))
#     names.append('last name')
#     print(names)

# everything is good!
# names_list(['Mahdi', 'Amir', 'Ali'])
# names_list(['Fatemeh', 'Mona', 'Nahid'])

# but ...
# names_list()
# names_list()
# names_list()

# solution
# def name_list_solution(names=None):
#     if names is None:
#         names = []
#     names.append('last name')
#     print(names)

# name_list_solution()
# name_list_solution()
# name_list_solution()


# --------- return statement ---------


# return terminates the function
# def x(a, b):
#     print(a + b)
#     print(a * b)
#     return
#     print('after return')

# x(10, 12)

# pass data back to the caller
# def addition(x, y):
#     return x + y

# add = addition(10, 20)
# print(add)

# no retutn -> None
# def addition(x, y):
#     result = x + y
# add = addition(10, 20)
# print(add)

# def user_info_to_list(name, age, email):
#     return [name, age, email]

# user = user_info_to_list('mahdi', 22, 'm@gmail.com').pop(0).title()
# print(user)
# user_name, user_age, user_email = user
# print(user_name)

# return special value None for use in conditional statements
# def check_even_number(x):
#     if x % 2 == 0:
#         return True

# number = 13
# if check_even_number(number):
#     print('yes,', number, 'is even')
# else:
#     print('No,', number, 'is not even')


# def f(x, y):
#     return x * y

# def h(x):
#     return math.sqrt(x)

# def g(x):
#     return x ** 3

# result = g(  h(   f(10, 10)    )   )
# print(result)
