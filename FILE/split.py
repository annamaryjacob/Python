#To print each number separately when the numbers are separated by a ','

f=open("/home/anna/Python/FILE/nums")
lst=list()
for item in f:
    num=item.split(",")   #the data is stored in list 'num'
    for n in num:         # the list 'num' is iterated
        print(n)