import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
# findall returns all the instances of the sub
print(x)
x = re.findall("Portugal", txt)
print(x)

x = re.search(r"\s", txt)
print(bool(x))
print(x.span())
print(x.group())
print(x.start())

x = re.sub("\s", "_", txt)
print(x)

data = 'from chahak2003jain@gmail.com 05-10-2022 09:10:22'
print(re.search("@.*", data).group().split()[1])
print("-----")
txt = 'I have submitted my report to the department on 12-12-2002,12122022'
x = re.search("([0-9]{2}-[0-9]{2}-[0-9]{4})", txt)
print(x.group(1))

txt = "I have submitted my report to the department on 12-12-2022,12122022"
print(re.findall(r"\b[aeiouAEIOU]\S*", txt))


txt = "a123456789abcd"
print(re.findall("[^a-z]*", txt))

txt="a123456789 2222 12"
print(re.findall("a?",txt))
