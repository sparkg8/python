list = ["uno", "dos", "tres", "cuatro", "cinco"]
list2 = ["banana", "cherry", "apple"]

print(list[-4:-1])
print(list[2:4])

# Change a value
list[1] = "2"
print(list)

# change a range
list[3:4] = ["x", "y"]
print(list)

# Change negative index
list[-1] = "5"
print(list)

list2[1:3] = ["watermelon"]
print(list2)

# Insert() method
list2.insert(3,"Pear")
print(list2)

# with append() to add elements at the end of the list
list2.append("Orange")
print(list2)

# Add a entire list to another list extend()
vegetables = ["Ltuce", "Tomatoe", "Brocoli"]

list2.extend(vegetables)
print(list2)

# Adding an iterable items into the list
# Tuples, Dicts, Sets
my_tuple = ("Guayaba", "Blueberry")

list2.extend(my_tuple)
print(list2)

# Remove elements: clear(), remove(), pop(), del

list2.pop() # removes the last item
print(list2)

list2.remove("Pear") # Removes the specified item "Pear"
print(list2)

#del list[0] # Removes the index 0 element: del list delete all the items
print(list)

#list.clear()
print(list)

"""
loop lists
"""

list3 = ["apple","banana","cherry"]


print("==============================================================")
# For loop printing item one by one
for item in list3:
    print(item)

# For loop using index
for index in range(len(list3)):
    print(list3[index])

print("============ while ===================")
i = 0
while i < len(list3):
    print(list3[i])
    i += 1

print("=========== Accessing through list Comprenhension ===========")
[print(x) for x in list3]

# Without list comprehension, create a new list with the elements in list that start with letter 'c'
new_list = []
for letter in list2:
    if "a" in letter:
        new_list.append(letter)

print(new_list)

# Same as avobe but using shorter syntax, 'List Comprehension
new_list = [word for word in list2 if 'o' in word]
print(new_list)

# Sort lists
# Ascending alphabetic order
list3.sort()
print(list3)

# Descending alphabetic order, use reverse()
list3.reverse()
print(list3)

# Sort with key function
list3.sort(reverse=True)
print(list3)

print("___")
# Return the number of elements with that specified value
print(list3.count("banana"))

#Return the index corresponds to that specified value
print(list3.index("apple"))

# JOIN Lists
# Concatenate symbol '+'
print(list + list2)

# Join with append()
for item in list:
    list3.append(item)

print(list3)

# Join with extend(), is iterable so need a 
numbers = [1, 2, 3]

numbers.extend(list)
print(numbers)


print(list3[-1])

print("====================")
print(list3)
print(list3[3::])# format is [start:end:steps] - > steps default value is 1



