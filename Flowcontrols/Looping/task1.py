no1=int(input("Enter first number"))
no2=int(input("Enter second number"))
if((no1%2==0)&(no2%2==0)):
    for i in range(no1,no2+1,2):
        print(i)
elif((no1%2==1)&(no2%2==0)):
    for i in range(no1+1,no2+1,2):
        print(i)
elif((no1%2==1)&(no2%2==1)):
    for i in range(no1+1,no2,2):
        print(i)
else:
    for i in range(no1,no2,2):
        print(i)
