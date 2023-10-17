message = 'Hi there, this is a string with single quotes'
print(message)

message = "Hi there, this is a string with double quotes"
print(message)

message = "It's a string"
print(message)

message = '"Beautiful is better than ugly", says Tim Peters'
print(message)

# Creating multiline strings
student_details = ''' 
Campus Details: MUBS Nakawa
    -Student name: Olaki Edwin
    -Student number: 2100706601
    -Phone number: 0787499401
    -Programme: BBC
'''
print(student_details)

# Using variables in Python strings with the f-strings
name = "Olaki Edwin Oryokot"
message = f'Hi {name}'
print(message)

# Concatenating Python strings
greeting = "Hello BBC " "Good Morning"
print(greeting)

greeting = 'Good afternoon, '
student = 'Edwin'
print(greeting + student)

# Accessing string elements
str = "Business Computing"
print(str[0])
print(str[1])

str = "Business Computing"
print(str[-1])
print(str[-2])

# Getting the length of a string
str = "Python String"
str_len = len(str)
print(str_len)

# Slicing strings
str = "Python String"
print(str[0:2])

# Python strings are immutable
str = "Python String"
new_str = "J" + str[1:]
print(new_str)

# Underscores in numbers
count = 10_000_000_000
print(count)
