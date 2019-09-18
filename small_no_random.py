"""
Use random module to get three numbers in three variables.
Print all three numbers.
Find the smallest number out of them in result variable.
print result.
"""
from random import randint

v1 = randint(99,300)
v2 = randint(44,66)
v3 = randint(7,14)
print("Three variable are: ", v1, v2, v3)
res = 0
if v1 < v2:
    res = v1
    print(res,"is smallest number")
else:
    res = v3
    print(res,"is smallest number")





