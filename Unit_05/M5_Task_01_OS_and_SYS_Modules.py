#OS and SYS modules

import os
import sys

#Get the current working directory(CWD)
cwd=os.getcwd()
print("Current working directory",cwd)

#Changing the current working directory
def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()

current_path()

#Changing the Cwd
os.chdir('../')

#Printing CWD after change
current_path()

#Make your own directory
directory="chahak"
parent_dir=os.getcwd()
path=os.path.join(parent_dir,directory)
os.mkdir(path)

#Remove a file
file="abc.txt"
path=os.path.join(parent_dir,file)
os.remove(path)

#Remove directory(Don't run in source code folder)
#directory="chahak"
# path=os.path.join(parent_dir,directory)
#os.rmdir(path)

####SYS Module#####
'''
The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python rumtime environemnt.
-sys.version is used which returns a string containing the version of Python Interpreter with some additional information.
-This shows how the sys module interacts with the interpreter
'''

import sys
print(sys.version)

#Input and Output using sys
'''
#stdin:
# -It can be used to get input from the command line directly.
# It, also,automatically adds '\n' after each sentence.
'''

import sys
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input:{line}')

print('Exit')

'''
#stdout:
-A built-in file object that is analogous to the interpreter's standard output stream in Python
-stdout is used to display output directly to the screen console.
'''
import sys
sys.stdout.write('Chahak Jain')
sys.stdout.write('Chahak Jain')
sys.stdout.write('Chahak Jain')
sys.stdout.write('Chahak Jain')
sys.stdout.write('Chahak Jain')
sys.stdout.write('Chahak Jain')
sys.stdout.write('Chahak Jain')

# end=" "
'''
-By default , the print function ends with a  new line.
-Passing the whitespace to the end parameter (end=' ')indicates that the end character has to be identified by whitespace and not a newline'''


