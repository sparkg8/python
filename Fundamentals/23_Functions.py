"""
A function in Python is a block of code to do instructions and can have parameters as inputs
is only executed when it is called.
Is declared with the keyword def
"""


def my_function():
    print("This is a function declaration.")


# Call the function to be executed here
my_function()

"""Notice, this does not return anything just does something"""
# passing parameters (parameter in def block and Arguments when call the function)


def my_return_function(param):
    print(f"This is my lucky number {param}")


# Call the function and pass number into it
my_return_function(7)

# Issue in order of the arguments, fn uses the arg. in a wierd way.
my_return_function('GAZELLE')  # Prints this: My lucky number is GAZELLE,
# to fix it we need to use keword arguments when passing the arguments

"""Positional arguments, with keyword arguments"""


def my_new_function(name='Gazelle', price=1499, brand='Adidas'):
    print(
        f"My favorite tenis shoes are the: {name} by {brand} their price is ${price}\n")


my_new_function()
my_new_function(name='Jordan', brand='Nike', price='1999')

# Accept any number of parameters with Arbitrary keyword arguments **kwargs


def my_third_function(**kwargs):
    """arbitrary keyword arguments"""

# The passed arguments are break into name and a value, and print items of the dictionary key:value
    for name, attack in kwargs.items():
        print(f"The attack to prcatice is: {attack}")


# Calling function and passing arguments
my_third_function(
    arm_attack="kimura",
    neck_attack="arm triangle",
    leg_attack="ankle lock",
    body_attack="charge"
)

""" Cleaner way to pass arbritary keywordargs is creating a dictionary key:value"""

attacks_d = {
    "arm_attack": "kimura",
    "neck_attack": "arm triangle",
    "leg_attack": "ankle lock",
    "body_attack": "charge"
}
print("========================**kwargs========================")


def arb_args_dictionary(**argu):
    """ using a dictionary """

    for key, value in argu.items():
        print(f"These are the attacks: {key}")


arb_args_dictionary(**attacks_d)

print("======================== Function return something ========================")


def attack_location(technique):
    # pass a list of attacks
    attacks = {"arm_attack": "kimora",
               "leg_attack": "ankle lock", "neck_attack": "arm triangle"}
    if technique in attacks:
        return attacks[technique]
    return "Unknown"


# call the function argument is the key_name in attacks dictionary
# I does exist so return value of that key_nme
print(attack_location("arm_attack"))
# Does not exist in dictionary so return a message Unknown
print(attack_location("head_attack"))

""" For next example a previous function attack_location is going to be the argument of current function"""


def multiple_attacks(atk_loc):
    # define new entries
    attack_new_list = ["head_atack", "chest_atack", "arm_attack"]
    for attack in attack_new_list:
        atk_loc = attack_location(attack)
        print(f"The new listed attack is location: {atk_loc}")


multiple_attacks(attack_location)


"""
return
"""


def add_two_numbers(num1, num2):
    return num1 + num2


add_two_numbers(2, 4) # here eventhough we called the function did not print the result, we need to assign it to a variable
result = add_two_numbers(3, 4)
print(f"Result: {result}")

"""Function that do a concatenation if arguments are string, and add them if both number's data type is int"""

def two_number_type(a ,b):

    if isinstance(a,int) and isinstance(b,int):
        print("Both enties are integer data type, adding numbers:\n")
        addition = a + b
        return addition
    elif isinstance(a,str) and isinstance(b,str):
        print("Entered values are both string data type, concatenating them:\n")
        concat = a + b
        return concat
    else:
        return "Different data type"
    

# Calling the function
#a = eval(input("Input for a value: "))
#b = eval(input("Input for b value: "))

#results = two_number_type(a, b)
#print(results)


"""
Simplest way to do above function
"""

def add_inputs(value1, value2):
    if type(value1 == value2):
        return value1 + value2
    else:
        return "The inputs are different data type"
    

# Call the function
#val1 = eval(input("Enter a value: "))
#val2 = eval(input("Enter a second value: "))

#answear = add_inputs(val1, val2)
#print(answear)

"""

POSITIONAL ARGUMENTS:
If I have parameters like (item, price), but when calling the function I pass values in different position
like this (50, "Water") they will print with any error at all and could cause wrong information.

To fix this and avoid confussion, we use the keyword arguments like (item="Water", price=50)

DEFAULT ARGUMENTS:
In the function definition, use the parameter with a value assigned, def function(item, price=60): price has a default parameter
and when call the function you can do it even without passing arguments.

ARBITRARY ARGUMENTS (*args):
These are used when you don't know the number of arguments are going to be passed to the function. A TUPLE is created
def student(name, class, *grades)

ARBITRARY KEYWORD ARGUMENTS (**kwargs):
The number of keyword arguments is unknown. A dictionary is created.

"""
# Default parameters
def store(item="Apples", price=60):
    print("Item: ", item)
    print("Price: ", price)

store(item="water") # the printout is Item: water, Price: 60
#Specifying arguments
store(item="lemon", price=19)
# using the default values
store()


"""                               *args                               """
def student1(name, clas, *grades):
    print("Name: ", name)
    print("Class: ", clas)
    #(M, P, A) = grades
    #print("Grades: ", grades)
    for x in grades: # access the values in the tuple
        print("Grades: ", x)


student1("Gema", 10, 100, 90, 80) # prints 100,90,80 in a tuple for the third parameter *grades

"""                               **kwargs                            """

print(":::::::::::::::: Keyword arbitrary args :::::::::::::::::::")
def student2(name, clas, **grades):
    print("Name: ", name)
    print("Class: ", clas)
    for k,v in grades.items(): # access the key:value in the dictionary
        print(k+": ",v)

# call the function
student2("Judit", 20, Art=100, Photoshop=90, Drawing=80)


"""
SCOPE OF THE VARIABLES:


"""
x = 10 # are declared in the global so can be used anywhere, and for any function
y = 20

def numbers(x, y):
    global z 
    z= 50 # This is a local to this function not usable outside
    print(x)
    print(y)
    print(z)

numbers(x, y)

print("--------------------")
print(x)
print(y)
print(z) # error z is not defined, is defined locally inside a function, declared as 'global'