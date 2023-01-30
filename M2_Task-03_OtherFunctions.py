# Q1. sum of number digits in list
sum = 0
lst = [1, 2, 3, "A", "hello", 123.5, 4, 5, 6, 7, 8, 9]
for i in lst:
    if (type(i) == int):
        sum = sum+i
print(sum)

# Q2.--------------------------------------------------------------------------------------------------
lst = ["this is amit", "this is amit!", "this is lamit..", "this is lamit??"]
result = []
K = "A"
for i in lst:
    l = i.split()
    for j in l:
        if j[0].lower() == K.lower():
            result.append(j)
print(result)

# Q3.----------------------------------------------------------------------------------------------------------------------------
lst = ["this is amit", "this is amit!", "this is amit..", "this is amit??"]
result = []
K = "t"
for i in lst:
    l = i.split(K)
    result = result+l
print(result)

# Q4
s = "However, Ram has been in the news for all the wrong reasons too.Illiterate bigots have weaponized the slogan Jai Shri Ram forwanton acts of violence, crime and hatred, which are anathema towhat Ram actually stands for. These lumpen elements do not knowthat Ram is maryada purushottam, the epitome of rectitude, thetouchstone of impeccable behaviour, the role model of the perfecthuman being, and the very incarnation of saumya rasa, harmoniouequilibrium."
l = s.split(" ")
print(l)
count = 0
n = 0
for i in l:
    if (i == "Ram" or i == "Ram."):
        count = count+1
print(count)
n = l.count('Ram')
print(n)

# Q5
s1 = s.replace('Ram', 'Shree ram')
print(s1)
# Q6
lst = s1.split(" ")
lst.sort(reverse=True)
print(lst)
string = ""
for i in lst:
    string = string+i+" "
print(string)
s3=string.rstrip()
print(s3)

#Q7
lst=[1,2,11,3,4,5,7,6]
temp=lst.copy()
temp.sort()
print(lst)
print(temp)
if(lst==temp):
    print("list is sorted")
else:
    print("Not sorted")

