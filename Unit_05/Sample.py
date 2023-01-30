# sys.argv:
'''
#sys.argv: command line argumentd:
-Command-line arguments are those which are passed during the calling of the program along with the
calling statement.
'''
import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("\nName of python script:", sys.argv[0])

print("\nArguments passed:", end="")
for i in range(1, n):
    print(sys.argv[i], end=" ")

# Addition of numbers
sum = 0

for i in range(1, n):
    sum += int(sys.argv[i])

print("\n\nResult:", sum)

#Q1.
'''
-WAP in python to check if the entered number is prime or not using command line argument technique

Also use square root technique to check if it is prime or not
'''
import math
import sys
def primeornot(l):
    value=math.ceil(math.sqrt(l))
    for i in range(2,value+1):
        if l%i==0:
            return "Not Prime"

    return "Prime"

result=primeornot(int(sys.argv[1]))
print(result)