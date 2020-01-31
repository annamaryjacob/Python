no1=int(input("Enter a value"))
no2=int(input("Enter a value"))
lst=[10,20,30,40,50,60]
try:
    ans=no1/no2
    print(ans)
    print("I have a debit transaction")
    print("I ate an icecream")
except Exception as a:
    print(a.args)

val=int(input("Enter an index value"))
try:
    print(lst[val])
except Exception as b:
    print(b.args)
finally:
    print("YAAAAAAAAAYYYYYYYY")
#here the programme if it cannot be excuted inside the try then it automatically goes to the except , so the promgramme does not stop
#-before execution
#for each change of exception put the code in another try and execute
#not depending on whether an exception has occurred or not, the finally block will be excecuted