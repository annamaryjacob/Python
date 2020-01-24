word="bat cat ball cat bat bill cat dog ball cat"
spl=word.split(" ")
lst=()
dic={}
for val in spl:
    if(val not in dic):
        dic[val]=1
    else:
        dic[val]+=1
tmp=list()
for k,v in dic.items():
    tmp.append((v,k))
prt=sorted(tmp,reverse=True)  #to sort the list in the descending order
print(prt[0])
# or use print(tmp[-1][1]) to print the last value of the list and only the 'cat' part

