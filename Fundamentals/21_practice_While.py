"""
While loops 
"""
# Break statement
i = 1
j = 0

while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Continue statement - Will stop at the current iteration and continue
while j < 6:
    j += 1
    if j == 3:
        continue
    print("continue:", j)

# Else in a while loop
i = 0
while i < 6:
    i += 1
    print(i)
else:
    print("i is no longer less than 6. ")

"""Print a string 5 times"""
print('My name is: ')
i = 0
while i < 5:
    print('My name five times ' + str(i))
    i += 1

s = 'socket0'
c = 'pxp3'
p = 'port0'

print(s, c, p, sep='.')
