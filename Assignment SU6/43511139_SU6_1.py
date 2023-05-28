#43511139 Nhlanhla Nwariwe
# This purpose of this program is to help the user determine the area, volume and diagonal of a triangular prism that has a base, perpendicular length and height supplied by the user.

import math
print("Cuboid calculator")
#code for the Base, Lenght, height and width
B=float(input("Enter the base(cm):"))
L=float(input("Enter the lenght(cm):"))
H=float(input("Enter the height(cm):"))
W=B
area=B*L+L*H+B*H+H*(math.sqrt(L**2+B**2))
diagonal=math.sqrt(L**2+W**2+H**2)
volume=L*B*H/2

print("Area of the triangular prism is ",round(area,4) , " square cm","\n"
      "Space diagonal of the triangular prism is ",round(diagonal,3),"cm","\n" 
      "Volume of the triangular prism is ",round(volume,2),"cubic cm")