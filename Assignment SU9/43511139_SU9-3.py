#43511139 Nhlanhla Nwariwe
email=input("Insert email address: ")
for i in range(len(email)):
    if email[i]=="@":
        name=email[:i]
        domain=email[i+1:]
        print("Name of email:",name)
        print("Domain of email:",domain)