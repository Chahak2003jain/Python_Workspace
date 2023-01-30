from tkinter import Y


def my_function():
    print("Hello from a function")
print("Out of the function")

my_function()

#Function with parameters
def my_function(fname):
    print(str(fname)+" reference")

my_function("Emil")
my_function("Password")
my_function(123)
my_function(1)
my_function(1.2)


def my_function(fname,lname):
    print(str(fname)+" "+lname )

my_function("Emil","Password")

#Arbitry Arguments,*args
def my_function(*kids):
    print(kids[2])

my_function("Ravi","Sumit","Amit")
my_function("Ravi","sumit","Amit","Ankush")
#my_function("Ravi","Sumit")     #tuple index out of bound issue
my_function("Ravi",123,123.4,'A')


#Keyword Arguments
def my_function(child3,child2,child1):
    print("Youngest child "+child3)

my_function(child1="Rashmi",child2="Chahak",child3="kajal")

#Default value of function parameter
def my_function(country="Norway"):
    print("I am from "+ country)

my_function("Switzerland")
my_function("India")
my_function()          #if we do not provide any argument then default argument will automatically pass to function
my_function("Brazil")

#Passing a list as an argument
def my_function(food):
    for i in food:
        print(i)

fruits=["apple","banana","cherry",123,123.4]

my_function(fruits)

#Return values
def add( a, b):
    return (a*b)

print(add(2,3))

#Pass function
def myfunction():
    pass

myfunction()
# python -m pydoc--for python documentation

