f=open("/home/anna/Documents/Python/fakefriends.csv")
dic={}
lst=[]
for item in f:
    word=item.rstrip("\n").split(",")
    for age in word:
      if (word[2] not in dic):
           dic[word[2]]=1
      else:
           dic[word[2]]+=1
print(dic)
temp=list()
for x,y in dic.items():
    temp.append((y,x))
prt=sorted(temp,reverse=True)
print(prt)
print("The age group that most uses social media the most is",prt[0][1])
print("The age group that least uses social media the most is",prt[-1][1])

# n=2
# r=len(lst)
# age=[]
# while(n<=r):
#     for s in lst:
#         age.append(s[2])
#     n+=1



