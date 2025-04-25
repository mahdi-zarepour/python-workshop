"""
String data type

How to deal with characters in Python
"""

name = 'Mahdi'
family = "Zarepour"
city = 'Kerman'
story_part_one = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat.
"""

# print(name, family, 'from ', city)
# print(story_part_one)
# print(type(name))

# len() function
empty_string = ''

# print('length of empty_string: ', len(empty_string))
# print('length of name: ', len(name))

# ---------------
# Escape Sequences in Strings

# Suppress special character meaning
# property = 'Ali's car'
property = "Ali's car" # Use single quote into double quote
property = 'Ali\'s car'
backslash = '\\' # Print backslash(\)

# Use \ for escape 'Enter' or <newline>
story_part_two = 'Duis aute irure dolor in \
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla \
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in \
culpa qui officia deserunt mollit anim id est laborum.'

# print(property)
# print(backslash)
print(story_part_two)

# Apply special meaning to characters
tab = 'start:\ttab!'
new_line = 'line1: \nline2: new line!'

# print(tab)
# print(new_line)
