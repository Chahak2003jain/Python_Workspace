import re
txt="Hey this is Amit Chauhan,Software Engineer, amit.chauhan@gmail.com"
# . and \ ReGex
result=re.search("@.",txt)
print(result.group())

# #@.*Regex
result=re.search("@.*",txt)  # it will return all the characters present in string after the symbol(@. means to return the character just after the @ symbol)
print(result.group())        # only @ as parameter means 


result=re.search("@\d",txt)  # it is used to find the digits in string after the @ sign
print(result.group())

#[ ]= it defines the range of characters from where it have to find
#{}= it defines how many times we have to find the digits
result=re.search("@\d*",txt) # *(zero or more)it is optional that the character that we are finding it is optional to find the desired character
print(result.group())

result=re.search("@\d+",txt) # +(atleast 1 or more) means if i am finding anything(digit) then that (digit) atleast should present after the @
print(result.group())

result=re.search("@",txt)  # it will 
print(result.group())

########################## EXTRACTION OF DATE #####################
txt="I have submitted my report to the department on 12-12-2022,12122022"
x=re.search("([0-9]{2}\-[0-9]{2}\-[0-9]{4})",txt)  #{2} IT IS USED TO FIND OUT THE NUMBER OF DIGITS WE HAVE TO FIND
print(x.group())