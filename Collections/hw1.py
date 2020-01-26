lst=list()
n=1
while(n<=3):
    x=int(input("Enter a value"))
    lst.append(x)
    n+=1
print(lst)
ans=list()
a=lst[1]*lst[2]
b=lst[0]*lst[2]
c=lst[0]*lst[1]
ans.append(a)
ans.append(b)
ans.append(c)
print(ans)