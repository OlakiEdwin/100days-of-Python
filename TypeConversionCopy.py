# value = input('Enter Value')
# print(value)

# price = input('Enter the price ($):')
# tax = input('Enter the tax rate (%):')
# net_price = price * tax / 100
# print(f'The net price is ${net_price}')

price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')
net_price = int(price) * int(tax) / 100
print(f'The net price is ${net_price}')

# Getting the type of a value
>>> type(100)
<class 'int'>

>>> type(2.0)
<class 'float'>

>>> type('Hello')
<class 'str'>

>>> type(True)
<class 'bool'>


# The number 100 has the type of int
# The number 2.0 has the type of float
# The string 'Hello' has the type of str
# And the True value has the type of bool