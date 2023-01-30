#Tuple in Python
'''
-Unchangeable [Immutable]
-Tuple items are ordered
-Allow duplicate values
Use () to create tuple instead of []
'''

#Empty Tuple
from distutils.util import change_root


t1=()

t1=(1,2,3,4,5,'Chahak','A',123.4)
print(t1)

t1=1,2,3,4,5,6,6
print(t1)

#Again tuple can store different types of elements
thistuple=("apple","banana","cherry","maple",123,123.4)
print(thistuple)

#Accessing the tuple elements
t1=1,2,3,4,5,6
print(t1[3])
print(t1[:])

#list ->tuple
lst=[1,2,3,4,5]
t2=(lst)
print(t2)

t3=tuple(lst)
print(t3)

#Functions to process tuple:
t1=(1,2,3,4,5,6,6)
print(len(t1))
print(min(t1))
print(max(t1))
print(t1.count(6))
print(t1.index(2))

t1=sorted(t1,reverse=True)

print(sorted(t1,reverse=True))

'''We can not perform operations in tuple like:
-append()
-extend()
-insert()
-clear()
because tuples are immutable
'''

#SET
'''
-{} for set
-set is a collection which is unordered
-unindexed
-No duplicate members
[will automatically be delete the duplicate elements from the set]
'''

setV={"apple","banana","cherry","custard",123,123,4}
print(setV)

print("_SET_")
t1={2,1,3,5,5,9,9}

print(t1)
print(len(t1))
print(min(t1))
print(max(t1))
print(min(t1))
print(sorted(t1,reverse=True))
print(t1)

'''we cannot perform these functions in sets
-append()
-insert()
-extend()
because sets are immutable
'''

#Dictionary
'''
-It is a key value pairs
-Dictionary is a collection which is ordered
-changeable
-No duplicate members
'''
#Dictionary Items
car={"brand":"Ford","Model":"Mustang","year":1964}
x=car.keys()
print(x) #before the change

car["color"]="White"   #update value
car["brand"]="Ford123"   #update value-->trying to make duplicate key
x=car.keys()
print(x)  #after change

y=car.values()
print(y)

#Duplicates are not allowed
thisdict={
    "brand":"Ford",
    "Model":"Mustang",
    "year":1964,
    "year":2022,
    "year":2023,
}
print(thisdict)

#Removing keys
thisdict.pop("Model")
thisdict.popitem()
print(thisdict)

#Traversing dictionaries
thisdict={"brand":"Ford","Model":"Mustang","year":1964}
print()
print("dictionary:")
for x in thisdict:
    print(x)

print()
print("Keys: ")
for i in thisdict.keys():
    print(i,":",thisdict[i])

print()
print("Values: ")
for i in thisdict.values():
    print(i)