res=1
no1=int(input("Enter first number"))
no2=int(input("Enter second number"))
for i in range(no1,no2+1):
    for k in range(2,i):
        if(i%k)==0:
            res=res+1
            break
        else:
            res=0
    if(res!=1):
        print(i)

#programme to print all prime numbers from the 2 nos inputed





