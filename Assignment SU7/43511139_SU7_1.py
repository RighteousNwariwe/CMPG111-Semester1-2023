#Nhlanhla 43511139
#this program is going to allow users to enter their age and gender to see if they are eligible to vote
age=int(input("Please enter your age: "))
gender=input("Please enter your gender(M/F): ")

if age>= 18:
    print("You are eligible to vote")
elif age<18:
    print("You are not eligible to vote")

if gender=="M" and gender=="F":
   bool(True)
elif gender=="m" and gender=="m":
    bool(True)
elif gender!="M" and gender!="F":
    print("Invalid Gender")