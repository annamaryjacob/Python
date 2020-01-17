ans=0
no1=int(input("Enter first number"))
no2=int(input("Enter second number"))
for i in range(no1,no2+1):
    flag=1
    for k in range(2,i):
        if(i%k)==0:
            flag=0
            break
    if(flag==1):
        ans=ans+i
print("Sum of all prime numbers=",ans)

#Sum of all prime numbers between the inputed amount
