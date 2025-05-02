"""
Another parent/base class for Square and Triangle children classes

"""
class Shape:
    __color = None # private attribute color so will need getter and setter methods 

    # Create setter and getter
    def set_color(self, color):
        self.__color = color
    
    # getter
    def get_color(self):
        return self.__color
    
"""
- import this module on the derived classes
- ready to use the attribute color in the main code

"""