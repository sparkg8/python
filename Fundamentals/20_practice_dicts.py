"""
Dictionaries are data collection used to storage data in key:value pairs,
* No duplicate data allowed
* Are changeable
* Are Ordered
Are declared with curly brackets

"""

# Dict declaration
my_dict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
}

print(my_dict)
print(len(my_dict))
print(type(my_dict))

# To reference is with a key name
print(my_dict["brand"])

print(my_dict.get("model"))

# Display all the keys()
x = my_dict.keys()
print(x) # keys before modification

my_dict["color"] = "red"
print(x)

# Now display all the values, return a list with the values 
y = my_dict.values()
print(y)

# change the dict
my_dict["color"] = "black"
print(y)

# The items() method, retur a list with tuples for all items in the dict key:value pairs.
z = my_dict.items()
print(z)


# Update or change an item in the Dict
# 1- by refering to the key name
my_dict["color"] = "yellow"

# 2- using the update() method with parameters in key:value form
my_dict.update({"year":2020})

print(my_dict)

"""
To add items, we use same methods as above for changes,
just if the item already exists then is changed if don't exist then is added/created

"""
# Add item by referencing the key name
my_dict["Owner"] = "Gema"
print(my_dict)

#Add item with update() method
my_dict.update({"Cost":150000})
print(my_dict)

"""
Remove dictionary items
can be used methods like: 

pop() - specify the key name to be removed
popitem() - removes the last inserted item
del dict["key_name"] - delete the item with the specified key name
del dict - remove the entire dictionary, raise an exception because of that
clear() - Empty the entire Dict

"""

print(my_dict.popitem()) # prints the removed item which is the lastone inserted
my_dict.pop("Owner")
print(my_dict)

del my_dict["color"]
print(my_dict)

#my_dict.clear()
#print(my_dict)

"""
Looping a Dictionary

by default the return value with for loop are going to be the keys
there are methods to return the Values.

"""
# 
for x in my_dict:
    print(x)

# print values one by one
print()
for val in my_dict:
    print(my_dict[val])

# Copy a dictionary, with copy() method or with dict() built-in function
dict2 = dict(my_dict)
print(dict2)

dict3 = my_dict.copy()
print(dict3)

"""
Nested dictionaries. When you creat a dictionary that contains more dictionaries within

"""

myFamily = {
    "kid1" : {
        "name":"Jesus",
        "age": 8
    },
    "kid2" : {
        "name" : "Ana",
        "age" : 4
    },
    "kid3" : {
        "name" : "Gael",
        "age" : 5
    }
}

print(myFamily)

# Other way for nested dictionaries is create separate dictionaries then wrap those into a dictionary

kid1 = {
    "name" : "Pedro",
    "age" : 6
}

kid2 = {
    "name" : "Juan",
    "age" : 3
}

kid3 = {
    "name" : "Olga",
    "age" : 10
}

master_dict = {
    "kid1" : kid1,
    "kid2" : kid2,
    "kid3" : kid3
}

print(master_dict)

# to access in nested dictionaries, especify the dict and the key name
print(myFamily["kid3"]["name"])

print(master_dict["kid1"]["name"])

# some methods for dictionaries
print(my_dict.get("year"))
print(kid1.items())
print(my_dict.setdefault("country", "Mexico"))

my_dict.update({"model":"honda"})
print(my_dict)

