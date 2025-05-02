"""
Sets are data collection in Python that are used to asign multiple values into a single variable.

Are unchangeable, but you can update values by add/removing items
Are Unorder, you don't know what order the items will appear.
Don't allow data duplication
A Set can contain different data types: bool, str, numbers, etc.

For Sets the values True and 1 means same value, would be a duplication of data.
"""

# Declaring a set is with curly brackets 
my_set = {"apple", "banana", "cherry"}

# Declaration throughout the set() constructor
set2 = set(("watermelon", "kiwi", "blueberry")) # note the double round-brackets

demo_list = ["mango", "papaya", "pineaple"]

print(type(my_set))

# Get the size of a Set
print(len(my_set))
print(set2)

# Access a Set, is not indexed so use the word 'in' to check out an item
for item in my_set:
    print(item)

# Check is a value exists: True/False
print("cherry" in my_set)

# Add item with add() method: Noted that inserts the element ramdomly
my_set.add("watermelon")
print(my_set)

# Add Sets with update() method, update is for any iterable like list, dict, tuples, sets etc.(order is random)
my_set.update(set2)
print(my_set)

# Adding another iterable like a list
my_set.update(demo_list)
print(my_set)

"""
Removing elements, uses the methods
    remove() - specify the element 
    discard() - specify the element
    clear() - empty the entire set
    del - Delete the elements and the set
    pop() - Removes a random item

"""
# remove()
my_set.remove("papaya")
print(my_set)

#discard()
my_set.discard("watermelon")
print(my_set)

#pop()
my_set.pop()
print(my_set)

# clear
#my_set.clear()
#print(my_set)

# del - return an error 'my_set' is not declared, delete all
#del my_set
#print(my_set)
