"""
Assignment Operators

...

regular assignment vs walrus assignment

walrus :=
------
1-assign 2-return
"""

x = 10
y = 20
x += y
y *= x
# u += x # NameError


# you can’t use a regular assignment to assign a value to a variable
# within the context of an expression
# i = (p = 10 * 20) # SyntaxError
i = ((p := 10) * 20) # walrus in expression
# print(i, p, sep=' | ')

# print statement, ... 
# print(name) # NameError
# print(name = 'Hamid') # TypeError
# print(name := 'Ali') # walrus in print statement


# z := 10 # SyntaxError
print(z := 10)
z += z
print(z)

# without walrus
# r = input('Enter a number: ')
# r = eval(r)
# r = eval(input('Enter a number: '))
# if r > 10:
#     r = r * 100
#     print('new r is: ', r)
# else:
#     print('r is less than 10')

# with walrus
if (r := eval(input('Enter a number: '))) > 10:
        r = r * 100
        print('new r is: ', r)
else:
    print('r is less than 10')


# illegal use of walrus assignment
# a = t := 10
# a, b = t := 10, e := 12
# a = b = t := 10
# a = 10
# a += t := 11
# a = (o, l := 1054)
# a = (o = l := 2555)
