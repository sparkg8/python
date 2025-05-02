"""
Composition: I a stronger relationship between child object and parent object, where child object cannot
             exist without the parent object, is part of the parent object. (car cannot exixt without engine and wheels)

Aggregation: Is a weaker relationship, child objct has to do with the parent object but it is not part of it.
             child object can exist without parent object.

"""

# Create a Salary class which relates with an Employee
class Salary:
    def __init__(self, payment, reward):
        self.payment = payment
        self.reward = reward
    
    def anual_salary(self):
        return (self.payment * 12) + self.reward
    
# create another class Employee
# employee is a salary cathegory?, No, that's why we cannot use inheritace here, but Composition 
class Employee(Salary):
    def __init__(self, name, age, payment, reward): # here parameters for employee class (name, age), instantiating the object of Salary will be (name, age, payment, reward)
        self.name = name
        self.age  = age
        # create an object that instantiates the class Salary
        self.salary_obj = Salary(payment, reward) # set this parameters in the init

    # Create a method that uses the anual_salary parent's method
    def total_salary(self):
        return self.salary_obj.anual_salary() # child object 

# Create an object 
s = Employee("Gema", 35, 200000, 20000)
print(s.total_salary())
 



