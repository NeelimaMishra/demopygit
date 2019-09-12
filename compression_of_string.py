str1 = 'aaabbab'
count = 1
temp = ''
output = ''
for i in str1:
    if temp == '':
        temp = i
        continue
    if temp == i:
        count += 1
    else:
        output = output + temp + str(count)
        #print(output)
        count = 1
        temp = i
output = output + temp + str(count)
print(output)
