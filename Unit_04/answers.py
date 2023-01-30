import re
txt="hello everyone this is chahak jain"
print(re.findall("[aeiouAEIOU]\\b \s*",txt))

txt="hello everyone 2003this is 1234chahak jain"
print(re.findall("\\b[1-7]\S*",txt))

#to fetch data
txt="I have submitted my report to the department"
print(re.findall("(([1-2][0-9]|3[0-2])\.[0-1][0-2].\[0-9]{4})",txt))

import re
# Q1 write a python program to find out all the words that  ends with  a vowel
txt="Rashmi Kuliyal Rameshwari Kapoor jgjge hkggj ojsgsgh"
print(re.findall("\S*[aeiouAEIOU]\\b",txt))

# Q2 write a python program to find out all the words start with a digit.
txt="123rashmi 767kuliyal yujjbbj"
print(re.findall("\\b[0-9]\S*",txt))

# Q3. write a python program to fetch the date from a string and make sure out of range date should not be fetched.
txt="I have submitted my report to the department on 12.12.2022,12122022,40.34.2022"
x=re.search("([0-2][0-9]|[3][0-1]\.[0-1][0-2]\.[0-9]{4})",txt)
print(x.group())

#Q4. write a python program to fetch all the words which starts with a capital letter.
txt="Rashmi Kuliyal Rameshwari Kapoor jgjge hkggj ojsgsgh"
print(re.findall("\\b[A-Z]\S*",txt))

#Q5. write a python program that matches a string that has an a followed by either [A-Z] , [a-z] or [0-9]
txt="Rashmi Kuliyal Rameshwari Kapoor jgjge hkggj ojsgsgh"
x=re.search("a\w*",txt)
print(x)

#Q6. write a python program to search a string which start with y or Y or z or Z
