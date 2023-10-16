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
