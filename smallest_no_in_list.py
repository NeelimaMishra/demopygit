"""
v1 = 18
v2 = 200
v3 = 1
put all 3 variables in a list l1 then find smallest value from list and put in result variable.
"""
v1 = 91
v2 = 33
v3 = 10
l1 = [v1, v2, v3]
print("list is: ",l1)
small_num = None
for i in l1:
    if small_num == None:
        small_num = i
    elif small_num < i:
        pass
    else:
        small_num = i
print(small_num)

'''
#Other way of writing the same program
for i in l1:
    if small_num == None:
        small_num = i
        continue
    if small_num > i:
        small_num = i
print(small_num)
'''
