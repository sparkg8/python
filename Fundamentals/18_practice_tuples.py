"""
Tuple is a data collection declared with round brackets, and it is ordered and unchangeable 
allows data dupliction and is used to asign multiple items to a single variable.

"""

my_tuple = ("Apple", "Banana", "Cherry")
print(my_tuple)

# Tuple with a single element, must add a coma
tuple_2 = ("Grape",)
print(type(tuple_2))

tuple_3 = ("Pear") # This case without a coma, is treated like string
print(type(tuple_3))

print(my_tuple[-1])

# Check if an item exist
if "Banana" in my_tuple:
    print("This value exist")


# Tuples are unchangeable, so there is a w/a to update the values into a Tuple
# Converting the tuple into a list type and replace the element
list1 = list(my_tuple)
list1[1] = "kiwi"
my_tuple = tuple(list1)

print(my_tuple)

# Adding an item in the tuple
list2 = list(my_tuple)
list2.append("Watermelon")
my_tuple = tuple(list2)

print(my_tuple)

# Other method to add items, due to is allowed to add one tuple to another tuple
# then you can create a second tuple

my_tuple += tuple_2
print(my_tuple)

# Unpacking a Tuple
# Is basically extract the values back into variables
fruits = ("banana", "apple", "cherry")
(b, a, c) = fruits

print(a)
print(b)
print(c)

# Unpacking variables, when the number of variables is less than the number of values (*)
fruits2 = ("apple", "banana", "cherry", "watermelon", "pear")
(a, b, *c) = fruits2
print("___")
print(a)
print(b)
print(c)
