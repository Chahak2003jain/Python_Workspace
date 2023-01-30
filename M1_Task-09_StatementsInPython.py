x=int(input("please enter integers"))
#If else statement
if x<0:
    print('less than 0')
elif x==0:
    print('zero')
elif x==1:
    print('single')
else:
    print('more')

for i in range(1,5):
    print(i)

x=5
while(x>=1):
    print(x)
    x=x-1 

#break and continue
n=8
count=0
for x in range(2,n):
    if n%x==0:
        print("Not a prime") 
        count=count+1
        break
    else:
        continue
if count==0:
    print("It is a prime number")

def initlog():
    pass

initlog()

# while True:
#     pass

#match statement
cpuModel=str.lower(input("Please enter yout CPU model"))

match cpuModel:
    case 'celeron':
        print('forget about it and play minesweeper instead')
    case 'core i3':
        print('Good luck')
    case 'core i5':
        print('you should be fine')
    case 'core i7':
        print('have fun')
    case 'core i9':
        print('designed nice')
    case _:
        print('it is that even a thing')


#short circuit (lazy evaluation){minimal evaluation}
"""
when evaluating an expression that involves the or operator Python can sometimes determine the result without evaluating all the operands. This is called short-circuit evaluation or lazy machine
"""


