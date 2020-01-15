no1=int(input("Enter first number"))
no2=int(input("Enter second number"))
no3=int(input("Enter third number"))
if((no1>no2)&(no1<no3)):
    print(no1,"is the second largest number")
elif((no1<no2)&(no1>no3)):
    print(no1,"is the second largest number")
elif((no2>no1)&(no3>no2)):
    print(no2,"is the second largest number")
elif((no2<no1)&(no2>no3)):
    print(no2,"is the second largest number")
elif((no3<no1)&(no3>no2)):
    print(no3,"is the second largest number")
elif((no3>no1)&(no3<no2)):
    print(no3,"is the second largest number")
else:
    print("All numbers are equal")
