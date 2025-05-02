"""
Task:
    1. Take input from user (name, age, grades)
    2. Create a class with __init__ method and also create an action method display() to print attibutes
    3. Try using Arguments and Parameters with different objects

"""
MSG = """
======================================================
"""
"""
#Input from user
name = input("Name: ")
age = input("Age: ")
grades = input("Grades: ")


class Student:
    def __init__(self, name, age, grades):
        self.name = name # Initialize the values (variables)
        self.age = age
        self.grades = grades

    # Action method
    def display(self):
        print("Hello ", self.name)
        print("you are ", self.age)
        print("Your grades are: ", self.grades)


# Create an object (intance of the class)
student_obj = Student(name, age, grades) # We don't have any output printed yet (did not call the action/method display())
student_obj.display()
"""

"""
PRIVATE ATTRIBUTES
A private attribute is indicated with double underscore
    - Only can be access within the class
    - Can be changed representing a security concern
    - Avoid can be change it neet to use getter and setter methods to access and modify values.

"""
class CarSpeed:
    def __init__(self):
        self.speed = 10
        self.__new_speed = 80 # this is the private ttribute

    # Define getter method
    def get_att_speed(self):
        return self.__new_speed
    
    #Setter method
    def set_att_speed(self, speed): # should request as parameter the new value
        self.__new_speed = speed


# Create an object try accessing the private attribute
# 
carspeed_obj = CarSpeed()
#try accessing private attribute
#carspeed_obj.__new_speed # AttributeError: 'CarSpeed' object has no attribute '__new_speed'

# Try with getter function
print("Speed updated: ", carspeed_obj.get_att_speed())

# Modify the private attribute is possible (should not be)
carspeed_obj.__new_speed = 150
print(carspeed_obj.__new_speed)

# Correct way to change a private attribute value is defyning a setter method
carspeed_obj.set_att_speed(200)
print(carspeed_obj.get_att_speed())

print(MSG)


"""
INHERITANCE:
    - There is a Base class (parent) and derived classes (childs)
    - The Derived classes can use the methods declared in parent class

    ?TIP: To determine wether a class is a child class, use the word "is a ? "
        Example Base class Polygon, child classes Square and Triangle
        Is triangle a Polygon?
"""

class Polygon:
    # declare private attributes, note that constructor to auto call methods is no needed
    # because we don't have actions for Polygon class
    __width = None # None because the inputs are going to declare later
    __height = None

    # Define a setter method because the Base's attributes are private
    def set_values(self, width, height):
        self.__width = width
        self.__height = height

    # Create two getters one for each value to fetch
    def get_height(self):
        return self.__height
    
    def get_width(self):
        return self.__width
    
    """ create the first child class called Square that calculates the Area """
class Square(Polygon): # In the round-brackets is specified the Base Class
# Method to calculate the Area 
    def area(self):
        return self.get_height() * self.get_width()
    
""" Create  second child class named [Triangle] that calculates the Area """
class Triangle(Polygon):
    def area(self):
        return self.get_height() * self.get_width() * 1/2
        

# Instantiate an object, no from the base class(Polygon) but of the child class(Square)
# a = Polygon() # !!! AttributeError: 'Polygon' object has no attribute 'area'
a = Square()
a.set_values(10, 10)
print("The Square's area is: ", a.area())

b = Triangle()
b.set_values(12, 10)
print("The Triangle's area is: ", b.area())

