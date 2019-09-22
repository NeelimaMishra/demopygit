str1 = 'aaabbab' # expected output should be a3b2a1b1; string compression
count = 0
temp = None
comp_str1 = ''

for i in str1:
    if temp is None:
        temp = i
        count += 1
        continue
    if temp == i:
        count += 1
        #comp_str1 = comp_str1 + temp + str(count)
    else:
        comp_str1 = comp_str1 + temp + str(count)
        count = 1
        temp = i
comp_str1 = comp_str1 + i + str(count)
print(comp_str1)




