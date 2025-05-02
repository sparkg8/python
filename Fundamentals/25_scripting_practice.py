""" 
Scripting. 
"""

"""Printing format"""

x = 3
y = 6
my_string = "Python Scripting"

# Recommended method to prinout
MSG = f'The "x" value is {x},\nthe "y" value is {y},\nand this is "{my_string}"'
#print(MSG)

#Other way to print with format
MSG2 = ('The "x" value is {}, \nthe "y" value is {},\nand this is "{}"' .format (x, y, my_string))
print(MSG2)

"""Basic calculator"""
#Simple addition
a = input("Enter a value: ")
b = input("Enter b value: ")

print(type(a))
print(type(b))

# Python evaluates the type of data
a = eval(a)
b = eval(b)

print(type(a))
print(type(b))

