x=int(input("Enter a number"))
for i in range(2,x):
    if(x%i==0):
        res=1
        break
    else:
        res=0
if(res==1):
    print("Number is not a prime number")
else:
    print("Number is a prime number")