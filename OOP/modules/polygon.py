"""
Base class Polygon
"""
class Polygon:
    __width = None
    __heihgt = None

    # Define setter to set the values
    def set_values(self, w, h):
        self.__width = w
        self.__heihgt = h
    
    # Getter to fetch values
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__heihgt

        