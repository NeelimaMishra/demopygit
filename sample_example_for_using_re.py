import re
str1 = '''
Jessica is 15 year old, and Dinel is 27 years old.
Edward is 97 and his grandmother , oskar is 102.
'''

age = re.findall(r'\d{1,3}', str1)
print(age)
name = re.findall(r'[A-Z][]a-z]*', str1)
print(name)

ageDict = {}
count = 0
for eachName in name:
    ageDict[eachName] = age[count]
    count += 1
print(ageDict)
