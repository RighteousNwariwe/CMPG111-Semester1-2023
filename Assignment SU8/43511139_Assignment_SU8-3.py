#43511139 Nhlanhla Nwariwe
#calculate the circumference of the shape
import math
_name=str(input("Please enter name: "))
print("Good day",_name,".")
_cir=int(input("Please enter the radius of the circle:"))
_side1=int(input("Please enter the side1 of the triangle:"))
_side2=int(input("Please enter the side2 of the triangle:"))
_side3=int(input("Please enter the side3 of the triangle:"))
l_sqr=int(input("Please enter the length of the square:"))
L_rec=int(input("Please enter the length of the rectangle:"))
W_rec=int(input("Please enter the width of the rectangle:"))

circum_cir=2*math.pi*_cir
circum_tri=_side1*_side2*_side3
circum_sqr=4*l_sqr
circum_rec=2*(L_rec+W_rec)
print("""
Shape                           Value(s)                                Perimeter
""")