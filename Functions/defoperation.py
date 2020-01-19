def thirdlar(no1,no2,no3):
    if((no1>no2)&(no1>no3)):
        print(no1,"is the largest number")
    elif((no2>no1)&(no2>no3)):
        print(no2,"is the largest number")
    elif((no3>no1)&(no3>no2)):
        print(no3,"is the largest number")
    else:
        print("All numbers are equal")

def prime(x):
    for i in range(2, x):
        if (x % i == 0):
            res = 1
            break
        else:
            res = 0
    if (res == 1):
        print("Number is not a prime number")
    else:
        print("Number is a prime number")

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
    print("Sum of all prime numbers=", ans)

def rev(n):
    i = 0
    rev = 0
    while (n != 0):
        dig = (n % 10)
        rev = (rev * 10) + dig
        n = n // 10
    print(rev)

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
            print(i)

def fact(i):
    n = 1
    res = 1
    while (n <= i):
        res = res * n
        n = n + 1
    print(i, "factorial is", res)

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

