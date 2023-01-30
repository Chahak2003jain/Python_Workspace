import math

def primeOrNot1(a):
    count=0
    for i in range(2,a):
        if(a%i==0):
            count=count+1
            break
    if count==0:
        print("It is a prime number")
    else:
        print("It is not a prime number")


def primeOrNot2(a):
    count=0
    for i in range(2,int(a/2)):
        if(a%i==0):
            count=count+1
            break
    if count==0:
        print("It is a prime number")
    else:
        print("It is not a prime number")

def primeOrNot3(a):
    count=0
    y=int(math.sqrt(a))
    for i in range(2,y+1):
        if(a%i==0):
            count=count+1
            break
    if count==0:
        print("It is a prime number")
    else:
        print("It is not a prime number")

def sqrt(a):
    i=1.0
    while(i*i<=a):
        i=i+1+.1
    

def primeOrNot4(a):
    count=0
    y=int(sqrt(1))
    for i in range(2,y+1):
        if(a%i==0):
            count=count+1
            break
    if count==0:
        print("It is a prime number")
    else:
        print("It is not a prime number")



x=input("Enter the value of x:\n")
primeOrNot1(int(x))
primeOrNot2(int(x))
primeOrNot3(int(x))
primeOrNot4(int(x))