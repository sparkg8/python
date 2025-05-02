"""
Example:
Get your own Python Server
Create a class named Person, with firstname and lastname properties, and a printname method:

"""

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    

    def printname(self):
        print(self.firstname, self.lastname)


#Use the Person class to create an object, and then execute the printname method:
obj_person = Person("Gema", "Gonzalez")
print(obj_person.firstname, obj_person.lastname) # without the print name function
obj_person.printname() # Caling the printname function

"""
Inheritance
When a derived (child) class can access all the methods and properties from a base class (parent).
"""

# child class
class Student(Person):
    def __init__(self, firstname, lastname, year): # we lost Inheritance, function init overrides the init of parent
        #Person.__init__(self, firstname, lastname) # recover Iheritane 
        super().__init__(firstname, lastname) # Same as above super() function helps to inherit automatically
        self.graduationyear = year

    
    def welcome(self):
        print("Welcome! ", self.firstname, self.lastname, " to the class of ", self.graduationyear)


# Here we used the method printname from Parent class (Person)
obj_student = Student("Jesus", "Garcia", 2019)
obj_student.welcome()


