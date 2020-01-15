no1=int(input("Enter First number"))
no2=int(input("Enter Second number"))
no3=int(input("Enter Third number"))
if(no1>no2):
    if(no1>no3):
        print(no1,"is the largest number")
    else:
        print(no3,"is the largest number")
else:
    if(no2>no3):
        print(no2,"is the largest number")
    else:
        print(no3,"is the largest number")
