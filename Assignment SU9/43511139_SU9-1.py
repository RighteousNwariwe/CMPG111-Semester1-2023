#43511139 Nhlanhla Nwariwe
#this is a program that counts in ascending order
num1=int(input("Please insert the first number: "))
num2=int(input("Please insert the last number: "))

#code
i=0

if num2<num1:
    print("Second number must be bigger than the first number!")
else:
    while i<=num2:
        for i in range(num1,num2+1,1):
            print (i)
            i+=1


