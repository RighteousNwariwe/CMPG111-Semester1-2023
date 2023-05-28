#Nhlanhla 43511139

import math
_num1=float(input("Please insert the first number:"))
_opp=input("Please insert an operator(+,-,*,/):")
_num2=float(input("Please insert the second number:"))

if _opp=='+':
    ans=_num1+_num2
    print("The calculated result: " ,ans)
elif _opp=="*":
     ans=_num1*_num2
     print("The calculated result: " ,ans)
elif _opp=="-":
     ans= _num1-_num2
     print("The calculated result: " ,ans)
elif _opp=="/":
    if _num2==0:
        print("Error – division by zero")
    else: ans=_num1/_num2
    print("The calculated result: ",ans)
  
else:
 print("Error – invalid operator ")


