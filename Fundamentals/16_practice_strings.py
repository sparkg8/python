"""
Practice methods and properties for strings 
"""

my_string = " Hello world, I'm a Python programmer!"

print(type(my_string)) # Devuelve el tipo "class_str"
print(my_string[13]) # Imprime lo que esta en la posicion 13 "I"
print(len(my_string)) # Longitud de la variable
print('programmer' in my_string) # Devuelve True


if 'programmer' in my_string:
    print('yes you are!')

print("Si" not in my_string) # Devuelve true/false en este caso es True. La palabra "Si" no está en la cadena
print("Hello" not in my_string) # Devuelve true/false en este caso es False. La palabra "Hello" si está en la cadena


""" SLICING STRINGS """

# Get characters from position 2 to position 5
print("1-4: ", my_string[1:4])

# Slice from the start
print("Start - 5: ", my_string[:5])

# Slice to the end
print("To the End: ", my_string[5:])

"""NEGATIVE INDEX
Are to start slicing the string from oposite direction, 
from the end to the begining
"""
# "Hello world, I'm a Python progra[mme]r!", starts at -2 position, but the -5 character is not taking care of
print("-5:-2 -> ", my_string[-5:-2])
print("-> ", my_string[-18:-12] ) # To print "Python"
#NOTA: El último indice ya no lo imprime por ejemplo: 1:4 imprimirá el dato de index 1,2,3 igual en los negativos.


"""
MODIFY STRINGS

"""
# strip() removes any whitespace at the begining and the end of the string
print(my_string.strip())

# replace() a string with another string
print(my_string.replace("programmer", "creative"))

# split() returns a list with the elements are between the specified separator, example ","
print(my_string.split(","))

# upper() turns in upper case the specified letter/word
print(my_string.upper())

# lower() turns in lower case the specified letter/word
print(my_string.lower())

# title() initializes the first letter as capital letter
print(my_string.title())

new_string = my_string.split(",")
number = 8
# Concatenate two strings a + "space" + b. string+number would be an error
print(new_string[0] + " " +new_string[1])

# Concatenate a String with a number. Use format or f
# print(new_string[0] + " " +number) <- TypeError: can only concatenate str (not "int") to str

# Usinf format() method, must use {} in the string text
# my_string = " Hello world, I'm a Python programmer! {}"
print(my_string.format(number))

# Format with "f" within the command line
print(my_string, f"{number}")

# Scape character \" to print double quotes: Hello "World"
print("Hello \"World\" ")




