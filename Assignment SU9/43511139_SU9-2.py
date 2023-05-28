#43511139 Nhlanhla Nwariwe
integer=int(input("Please insert an integer: "))
i=0
ans=0
total=0
for i in range(1,13,1):
    ans=i*integer
    print(i," x ",integer," = ",ans)
    total+=ans 

print("Sum of the totals= ",total)
