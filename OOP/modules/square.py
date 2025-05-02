"""
Declaration of child class Square 
"""
from polygon import Polygon
from shape import Shape #to inherit this class add the class name into the child class parenthesis

class Square(Polygon, Shape): # This Square class has two parent classes
    def area(self):
        return self.get_width() * self.get_height()
    
