import os
x=os.getcwd()
print(x)
x=x+'\\'

f=open(x+'file.txt','r')
# print("Enter data in a file")
# while(True):
#     x=input()
#     if(x=='-1'):
#         break
#     x=x+'\n'
#     f.write(x)
    
# n=int(input("Enter the value of n"))


#to read first n lines
# lines=f.readlines()
# for i in lines[:n]:
#     print(i,end='')


#to read last n lines 
# lines=f.readlines()
# for i in lines[-n:]:
#     print(i,end='')
    

#to find longest word
# lines=f.read().split()
# print(lines)
# l=[]
# for i in lines:
#     l.append(len(i))

# ind=l.index(max(l))
# print("Longest word:",lines[ind])
   
        
#to handle file not found exception
# try:
#     print("hanfling file exceptions")
#     file_name=open("Hello.txt",'r')
# except FileNotFoundError:
#     print("file doesn't exist in read mode..try in write mode")
#     file_name=open('hello.txt','w')
#     print("opened")
# else:
#     print('jj')


#find unique no. of words in a file

lines=f.read().split()
print("--")
count=0
for i in lines:
    freq=lines.count(i)
    if freq == 1:
        print(i)
        count=count+1
print(count)     

#to handle none type of exception in python'

#to get the file size of a plain file
print("file size: ",os.path.getsize(x+'file.txt'))