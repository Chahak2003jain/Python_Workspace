
# '''PS E:\python_workspace> python -u "e:\python_workspace\Unit_01\M1_Task-08_StringsInPython.py"
# PS E:\python_workspace> python
# Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
#  George
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'George' is not defined
#  "George"
# 'George'
#  'George'
# 'George'
# '''

print('I\'m fine')
print('press "Enter"')
print('Red'+' '+'Car')
s="Chahak"
print(s[2::])

#compare two strings
s1="Helloo"
s2="hello"

if(s1==s2):
  print("Equals")
else:
  print("Not Equals")

if s1<=s2:
  print("s1 is smaller than equal to s2")
else:
  print("s2 is smaller than s1")

#Remove spaces from string
name=" Chahak Jain "
print(name.rstrip)
print(name.lstrip)
print(name.strip)
print(name)

#find a substring
str=input("Enter main string")
substr=input("Enter the substring")
n=str.find(substr,0,len(str))
if n==-1:
  print("Substring not found")
else:
  print("Substring found at position",n)

#string are immutable in python
'''
An imutable object is a object whose content can be changed. in python : strings , numbers and tuples are mutable
 '''
s1='one'
s2='two'
s1=s2
print(s1)
print(id(s1))
print(id(s2))


#Replacing  a substring
str="That is beautiful"
s1='beautiful'
s2='not beautiful'

str1=str.replace(s1,s2)
print(str1)

#Split function
stt=str1.split(' ')
print(stt)
for i in stt:
  print(i)

  #changing case of the string
#str="That is beautiful2"
print(str.upper())
print(str.lower())
print(str)


#superscript and subscript
numbers_to_letters=str.maketrans("123","ABC")
print(str)
print("Question 1,point 2 and 4".translate(numbers_to_letters))

subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
print("C2H5OH".translate(subscript))

superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
print("PIr2".translate(superscript))

superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
print("PIr2".translate(superscript).replace('PI', 'π'))












