#Alternate element in list

l1 = [5, 10, 15, 0, 7, 9, 11]

# one of the way of doing this program
new1_l1 = []
new2_l1 = []
flag = True
for i in l1:
    if flag == True:
        new1_l1.append(i)
        flag = False
    else:
        new2_l1.append(i)
        flag = True
print(new1_l1)
print(new2_l1)

#second approach
new_l1 = []
count = 0
while count < len(l1):
    new_l1.append(l1[count])
    count += 2
print(new_l1)

#third approach
odd_new_l1 = []
even_new_l1 = []
for i in range(0, len(l1), 2):
  odd_new_l1.append(l1[i])
for i in range(1, len(l1), 2):
  even_new_l1.append(l1[i])
print(even_new_l1)
print(odd_new_l1)
