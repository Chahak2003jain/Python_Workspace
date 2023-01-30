#Working of open() function
'''
Here file is a file object not a simple variable
file=open(filename with path,mode)
'''

#1. Manual approach to get the file path
path='E:\\python_workspace\\Unit_03'
path=path+'/'

file=open(path+'abc.txt','r')
for i in file:
    print ("i:",i)
print("============")
file.seek(0)
print(file.read())

#2 os.getcwd()
import os
path=os.getcwd()+"/Unit-03/"
print(path+"*")

#3
import os
path=os.path.dirname(__file__)
print(path)
path=path+'/'

'''
r: just to read a file
w: open an existing file in write mode, if the file already conmtains some data then it will be overidden,if not exists it will make a new file
a: open an existing file for append operation. It won't override
r+:To read and write data into file .The previous data in the file will also be overriden.
w+:Read+Write->Override result
a+: Read + Append + don't override
'''

#Write into a file (W)
file=open(path+'abc.txt','w')
file.write("This is write command")
file.write("It allows us to write in a particular file")
#file.seek(0)
print(file.read())

#opening file in append+ mode
file=open(path+"abcd.txt","a+")
file.write("12344")
file.seek(0)
# file=open(path+"abc.txt","r")
print(file.read())



# opening file in append mode(we cant read in the file)
file=open(path+"abc.txt","a")
file.write("12344")
# file.seek(0)
# # file=open(path+"abc.txt","r")
# print(file.read())

#opening a file in r+ mode
file=open(path+"abcd.txt","r+")  # it will throw an exception it cannot create a new file if does not exit
print(file.read())


#opening the  file in w+ mode
file=open(path+"abc.txt","w+")
file.write("12344")
file.seek(0)
# file=open(path+"abc.txt","r")
print(file.read())

#Renaming a file(Case Insensitive)
import os
path=os.path.dirname(__file__)
print(path)
path=path+'\\'
os.rename(path+"ABC.txt",path+"abc.txt")

"""
#Deleting a file(Case sensitive)
os.remove(path+"ABC.txt")
"""
file=open(path+"abc.txt",'r')
data=file.readlines()
print(type(data))
print(data)

for i in data:
    #print(type(i))#String
    words=i.split()
    #print(type(words))
