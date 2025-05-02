"""
Calculate the sum of numbers: Write a program that prompts the user to enter a positive integer 
and then calculates the sum of all the numbers from 1 to that integer using a for loop.
"""

range_num = int(input("Enter a positive number for a range: "))
sum = 0
output = ""

for number in range(1,range_num+1):
    sum = sum + number
    # print(number, "+ ", end="") # Output is with an extra '+' sign
    # Remove the extra '+' sign
    if number == 1:
        output += str(number) # Convert into string
    else:
        output += " + " + str(number)


print(output, " = ", sum)