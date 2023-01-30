import re

#words starting with vowel
str='i ama chahak s0123jain an@d good magsine'
a=re.findall(r'\b[aeiou]\S*',str)
print(a)

#words ending with vowel
a=re.findall(r'\S*[aeiou]\b',str)
print(a)

#words starting with digit
a=re.findall(r'\b[0-9]\S*',str)
print(a)

#words starting with y or s
a=re.search(r'\b[sy]\S*',str)
print(a.group())

#words which do not contain an special character
a=re.findall(r'\b[a-zA-Z0-9]*\b',str)
print(a)

#words which  contain an special character
a=re.findall(r'^\.*',str)
print(a)

#words which  contain an words with alphabets of len 3
a=re.findall(r'\b[a-zA-Z]{3}\b',str)
print(a)