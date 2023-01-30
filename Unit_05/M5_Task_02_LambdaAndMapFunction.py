#Lambda or anonymous functions in python
'''
-A lambda function is a small anonymous function.
-A lambda function can take any number of arguments
-It can create functions in one line when possible
'''

def add(a,b):
    return a+b

def minus(x,y):
    return x-y-2
    
minus=lambda x,y:x-y
print(minus(9,4))

#Q2.
'''
WAP in python to calculate the square root of a whole number by using lambda expression and math.sqrt technique
'''
import math
root=lambda a:math.sqrt(a)
print(int(root(25)))

#Map in Python
'''
-The map()  function executes a specified function for each item
-The item is send to the function as a parameter
'''

def myfunc(n):
    return len(n)

result=map(myfunc,("CAT","DOG","GOAT"))
# print(list(result))
print(list(result)[2])

a1=myfunc("CAT")
a2=myfunc("CATS")
a3=myfunc("CAT")
print(a1,a2,a3)

def myfunc(a,b):
    return a+b

x=map(myfunc,('apple','banana','cherry'),('orange','lemon','pineapple'))
print(list(x))

#Q3.
'''
WAP in python to check if the number is prime or not? Check multiple numbers at once(this line indicates that the program has to be done using map funnction)
'''
def primeornot(n):
    value=math.ceil(math.sqrt(n))
    for i in range(2,value+1):
        if n%i==0:
            return "not prime"
    return "prime"
x=map(primeornot,(7,8,9,10,12,18,56,19,17))
print(list(x))
#map function returns object

































