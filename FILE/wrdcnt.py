# f=open("/home/anna/Python/FILE/HI")
# dic={}
# lst=[]
# for item in f:
#     word=item.split(" ")
#     for num in word:
#         lst.append(num.rstrip("\n"))
# for d in lst:
#     if (d not in dic):
#         dic[d]=1
#     else:
#         dic[d]+=1
# print(dic)

f=open("/home/anna/Python/FILE/HI")
dic={}
lst=[]
for item in f:
    word=item.rstrip("\n").split(" ")
    for num in word:
      if (num not in dic):
           dic[num]=1
      else:
           dic[num]+=1
print(dic)
