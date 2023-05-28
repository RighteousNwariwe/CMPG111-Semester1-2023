#43511139 Nhlanhla Nwariwe
#Ascending order
pos_number=int(input("Please insert a positive number: "))
_newNumber=0
ans=0
while _newNumber<=pos_number:
        print(_newNumber)
        ans +=_newNumber
        _newNumber+=1
#sum of integers
print("Sum for the integers:")

for x in range(pos_number):
    if x!=pos_number:
          print(x,"+", end=" ")
    else:
        print(x,"=",ans)
