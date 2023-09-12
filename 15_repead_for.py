"""
Ask to the user for a list or numbers and print the greatest
"""
usr_list = input("Type a list of numbers separated by a coma: ")
numbers = [int(i) for i in usr_list.split(',')]# Convert string into integer numbers
temp = numbers[0]

for number in numbers:
    if temp < number:
        temp = number
    else:
        continue
print("The greatest number is: ", temp)

