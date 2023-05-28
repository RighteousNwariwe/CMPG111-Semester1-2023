#43511139 Nhlanhla Nwariwe
#Solving the Quadratic equation

#User input
import math
print("Solving ax^2 + bx + c=0")
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))

#calculation
x1=(-b+math.sqrt(b**2-4*(a)*(c)))/(2*a)
x2=(-b-math.sqrt(b**2-4*(a)*(c)))/(2*a)

print("ROOTS OF GIVEN QUADRATIC EQUATIONS ARE:")
print("x1:",x1)
print("x2:",x2)