"""
Main script

Double inheritance would be example:
    Triangle is a shape, triangle is a polygon (yes) 
    so Triangle will inherit from two parent clases Polygon/Shape

"""
import square as s
import triangle as t
#import shape #no need because is already imported on the square and triangle modules, we just need to import those

print()
MSG = "=========================================="

print(MSG)
# Instantiate the Square class with object sq
sq = s.Square()
sq.set_values(6, 6)
sq.set_color("Red")
print("The Square's area is: ", sq.area())
print("Color: ", sq.get_color())

print(s.Square.__mro__) # sequence of classes and obj are being executed

print(MSG)
tr = t.Triangle()
tr.set_values(5, 6)
tr.set_color("Turquise")
print("The Triangle's area is: ", tr.area())
print("Color: ", tr.get_color())

print(MSG,"\n")
