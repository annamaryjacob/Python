def thirdlar(no1,no2,no3):
    if((no1>no2)&(no1>no3)):
        ans=no1
        return ans
    elif((no2>no1)&(no2>no3)):
        ans=no2
        return ans
    elif((no3>no1)&(no3>no2)):
        ans=no3
        return ans
    else:
        ans="All numbers are equal"
        return ans

def prime(x):
    for i in range(2, x):
        if (x % i == 0):
            res = 1
            break
        else:
            res = 0
    if (res == 1):
        ans="Number is not a prime number"
        return ans
    else:
        ans="Number is a prime number"
        return ans

def sumprime(no1,no2):
    ans = 0
    for i in range(no1, no2 + 1):
        flag = 1
        for k in range(2, i):
            if (i % k) == 0:
                flag = 0
                break
        if (flag == 1):
            ans = ans + i
    res=ans
    return res

def rev(n):
    i = 0
    rev = 0
    while (n != 0):
        dig = (n % 10)
        rev = (rev * 10) + dig
        n = n // 10
    ans=rev
    return ans

def listprime(no1,no2):
    res = 1
    for i in range(no1, no2 + 1):
        for k in range(2, i):
            if (i % k) == 0:
                res = res + 1
                break
            else:
                res = 0
        if (res != 1):
            ans=i
            return ans

def fact(i):
    n = 1
    res = 1
    while (n <= i):
        res = res * n
        n = n + 1
    ans=res
    return ans


def isoddeven(no):
    if(no%2==0):
        print("even")
    else:
        print("odd")

def posneg(no1):
    if (no1 < 0):
        print("Number is a negative number")
    else:
        print("Number is a positive number")

def fib(n):
    n1 = 0
    n2 = 1
    y = 0
    print(n1)
    print(n2)
    while (n >= y):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3)
        y = y + 1

def add(no1,no2):
    return (no1+no2)

def sub(no1,no2):
    return (no2-no1)

def mul(no1,no2):
    return (no1*no2)

def div(no1,no2):
    return (no2/no1)

def mod(no1,no2):
    return (no2%no1)

def pow(no1,no2):
    return(no1**no2)


