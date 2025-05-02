"""
Enter a list of numbers and print the greatest 
"""

user_input = input("Enter a list of numbers separated with a coma: ")
list_numbers = [int(i) for i in user_input.split(',')]
greatest_temp = list_numbers[0]

for number in list_numbers:
    if greatest_temp < number:
        greatest_temp = number
        #print(greatest_temp)
    #print(number)
print(greatest_temp, "es el numero mayor de la lista.\n")
