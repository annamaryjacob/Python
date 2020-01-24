line="Hi Hello Hi How Are You"
words=line.split(" ")
dic={}
for word in words:
    if(word not in dic):
        dic[word]=1
    else:
        dic[word]+=1
for item in dic:
    print(item,end=":")
    print(dic[item])
