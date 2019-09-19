# Sorting a list

l1 = [7, 6, 10, 0, 56, 2, 9]
count = 0
while count < (len(l1)-1):
    #import pdb; pdb.set_trace()
    for i in range(len(l1)-1):
        if l1[i] > l1[i+1]:
            temp = l1[i]
            l1[i] = l1[i+1]
            l1[i+1] = temp
    count += 1
print(l1)