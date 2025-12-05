name =  input("Enter your name ")
age = int(input("Enter your age "))
if(age>=18):
    print("Hi "+name+" You can take part in votting")
else:
    print("Sorry, you cannot take part because your age is"+str(age)+" year, you will be able to participate after "+str(18-age)+" year")
