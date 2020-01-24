inp="A B C B A B C A G"
val=inp.split(" ")
dic={}
for key in val:
    if(key not in dic):
        dic[key]=1
    else:
        print("First reccursive character is",key)
        break



