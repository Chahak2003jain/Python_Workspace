# Note
'''
-A RegEx ,Regular Expression ,is a sequence of characters that forms a search pattern.
-RegEx can be used to check if a string contains the specified search pattern.
-Python has a built-in package called "re", which can be used to work with Regular Expressions.
'''

import re
txt = "The rain in Spain"
x = txt.find("ai")  # This is not a RegEx function but a string function
print(x)

x = txt.find("ai", 7)  # starting index is 7
print(x)

# Import the re module

txt = "The rain in Spain"
x = re.findall("ai", txt)
# findall returns all the instances of the sub
print(x)

x = re.findall("Portugal", txt)
print(x)

# Search for the first white-space character or even a word in the string
txt = "The rain in Spain"
x = re.search(r"\s", txt)
y = re.search("rain", txt)
print(x)
print(y)
'''output-><re.Match object; span=(3, 4), match=' '>
<re.Match object; span=(4, 8), match='rain'>'''
print(y.span())  # returns the list of first and end index of search string->returns the span of the word/character
print(y.group())  # actual word/set from the result
print(y.start())  # position  of first occurence
print(y.end())  # will search from the end

# Split a statement , based on single space
txt = "The rain in Spain"
x = re.split("\s", txt)  # This will return a list of words
print(x)

# control the number of occurences by specifying the maxsplit parameter
txt = "The rain in Spain"
x = re.split(r"\s", txt, 1)
# x=re.split("\s",txt,1)[0]    ---> returns 'The' as output
print(x)

# The sub() function replaces the matches the text of your choice
txt = "The rain in Spain"
x = re.sub(r"\s", "_", txt)
print(x)

# Match Object in RegEx
txt = "The rain in Spain"
print("--------")
x = re.search("ai", txt)  # This will return an object Match
print(x)
print(type(x))
print(x.start())  # returns the starting index
print(x.span())  # returns the span of the word/character
print(x.group())  # actual word/set from the result
print(x.end())  # will search from the end

# Match Object
'''
-A Match Object is an object containing information about the  search and the result.
-If there is no match , the value None will be returned, instead of the Match Object.
'''
# Q1. Find host or domain name from text provided

# 1. First Approach(String function)
data = 'from chahak2003jain@gmail.com 05-10-2022 09:10:22'

loc = data.find("@")
print(loc)
eloc = data.find(" ", loc)
print(eloc)
print(data[loc+1:eloc+1])
# using RegEx
print(re.search("@.*", data).group().split()[0])

x = re.search("@.*", data)
print(x)
x = x.group()
print(x)
x = x.split()[0]
print(x)

# #using urllib.parse technique(not for students)
# from urllib import parse
# email='myemail@mydomain.com'
# user=parse.splituser(email)[0]
# domain=parse.splituser(email)[1]
# print(user,domain)

# Extract date from string
txt = 'I have submitted my report to the department on 12-12-2002,12122022'
x = re.search("([0-9]{2}\-[0-9]{2}\-[0-9]{4})", txt)
print(x.group())

# return all the words of a string that starts with vowel
txt = "I have submitted my report to the department on 12-12-2022,12122022"
print(re.findall("\\b[aeiouAEIOU]\S*", txt))
print(re.split(r"\s|,|\.", txt))
# enumerate all the world in a string to extract all the world in a string   S(it denotes non space characters)
# d=for digits
# D=for non-digits

# Q4 split the string with multiple delimeters
print("+++++++")
txt = "I have submitted my report to the department on 12-12-2022,12122022"
print(re.split(r"\s|,|\\.", txt))


# Q5 Return the first word of a given string
txt = "I have submitted my report to the department on 12-12-2022,12122022"
# x=txt.split(" ")[0]   using the method of string
# print(x)
print(re.split(r"\s", txt)[0])  # using regex


# Q6 Return all the words of a string
txt = "I have submitted my report to the department on 12-12-2022,12122022"
print(re.split(r"\s", txt))

#returns numbers used in string
txt = "123456789abcd"
print(re.findall("9\S", txt))

txt = "a123456789abcd"
print(re.findall("9\A", txt))

txt = "123456789abcd"
print(re.findall("[^a-z]*", txt))

txt="a123456789 2222 12"
print(re.findall("a?",txt))


# web scrapping-- beautiful soup
