no1=int(input("Enter First number"))
no2=int(input("Enter Second number"))
no3=int(input("Enter Third number"))
if((no1>no2)&(no1>no3)):
    print(no1,"is the largest number")
elif((no2>no1)&(no2>no3)):
    print(no2,"is the largest number")
elif((no3>no1)&(no3>no2)):
    print(no3,"is the largest number")
else:
    print("All numbers are equal")



