# Exception Handling
'''
#Exception ,Error, Compilation Issues
1. compilation Issues:
-syntax issues, or issues in the code
catch by the python compiler
pritn("chahak")
2. Exceptions:
-Issues in your code,catch by PVM(Python Virtual Machine)
-Run time issues, Handle [PVM]
a=10
b=0
print(a/b)
-Handling is possible by using try and except
-Exceptions are always handled by programmer
3. Errors:
-can not be handled by the programmer
-Happen at run time
-Even PVM can not catch them
Memory full,  Stack overflow, power failure etc,
-System Design should be robust and efficient
'''
path = "E:\\python_workspace\\Unit_03\\"
try:
    # we have to add suspicious code in try block
    file = open(path+"abc.txt", "w")
    file.write("abcd")
    a = int(input("Enter value of a"))
    b = int(input("Enter value of b"))
    c = a/b
except ZeroDivisionError:
    # handling of those exceptions
    print("b should not be zero")
    b = int(input("Enter value"))
    c = a/b
else:
    print("Else block of code")
    print(c)

finally:
    # this block will always run
    file.close()
    print("file is closed now")
print(c)
# 1.
