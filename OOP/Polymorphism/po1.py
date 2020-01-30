def add(no1):
    no2=20
    print(no1+no2)

def add(no1,no2,no3):
    res=no1+no2+no3
    print(res)

def add(no1,no2,no3,no4):
    res=no1+no2+no3+no4
    print(res)

#Function over loading
#same function but different number of arguments
#only the most rescently implememted function can be invoked
#ie, only add(1,2,3,4) can be invoked in this case

class math():
    def add(self,no1):
        no2 = 20
        print(no1 + no2)


    def add(self,no1, no2, no3):
        res = no1 + no2 + no3
        print(res)

    def add(self,no1, no2, no3, no4):
        res = no1 + no2 + no3 + no4
        print(res)

#Method over riding
#in this 'method' also only the most rescently implemented method can be invoked

