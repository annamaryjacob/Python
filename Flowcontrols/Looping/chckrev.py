i=0
rev=0
n=int(input("Enter the number"))
while(n!=0):
    dig=(n%10)
    rev=(rev*10)+dig
    n=n//10
print(rev)



