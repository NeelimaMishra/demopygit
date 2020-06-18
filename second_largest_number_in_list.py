# Program to find second largest number in a list

l1 = [-1, -2, 4, 0, 1, 8, 2]
count = 0
while count < 2:
    sec_lar = None
    for i in l1:
        if sec_lar is None:
            sec_lar = i
            continue
        else:
            if sec_lar < i:
                sec_lar = i
    #print("In 1st loop largest number is: ", sec_lar)
    l1.remove(sec_lar)
    count += 1
print("2nd largest number is: ", sec_lar)

#other way of doing this program
'''
l1 = [2,1,3]
largest = None
secondlargest = None
for i in l1:
    if largest is None:
        largest = i
        continue
    elif secondlargest is None:
        if i > largest:
            secondlargest = largest
            largest = i
        else:
            secondlargest = i
        continue
    if i > largest:
        secondlargest = largest
        largest = i
    elif i > secondlargest and i < largest:
        secondlargest = i
'''


