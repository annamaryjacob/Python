fl=open("/home/anna/Python/FILE/number")
lst=list()
for item in fl:
    if int(item)%2==0:
        lst.append(item.rstrip("\n"))
    else:
        pass
print(lst)

#to store list as integers use lst.append(int(item)) instead of rstrip