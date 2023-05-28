#Nhlanhla 43511139
import math
b=int(input("Please input the base: "))
e=int(input("Please input the exponent: "))

if e< 0:
    print("Error – exponent cannot be negative")
   
elif b==0 and e==0 :
    print("Error – indefinite form (0˄0)")
else :
     ans=b**e
     print("The calculated result: ",ans)