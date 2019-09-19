# sum of even and odd index element in list of given list.

l1 = [1, 100, 3, 4, 5, 6]

'''
#One way of doing this program is following
evenl1 = l1[::2]
print("Even index list is: ", evenl1)
sumeven = 0
for i in evenl1:
    sumeven += i
print(sumeven)
oddl1 = l1[1::2]
print("Odd index list is: ", oddl1)
sumodd = 0
for i in oddl1:
    sumodd += i
print(sumodd)
'''

sum_even = 0
sum_odd = 0
flag = True
for i in l1:
    if flag == True:
        sum_even += i
        flag = False
    elif flag == False:
        sum_odd += i
        flag = True
print("sum of even index in l1 is: ",sum_even)
print("sum of odd index in l1 is: ", sum_odd)

