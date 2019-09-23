str1 = 'Ab,c,de!$' # Expected output 'c,b$a'
temp_str = ''
for i in str1:
    if i.isalpha():
        temp_str = i + temp_str
print(temp_str) #cba
cnt = 0
out_str = ''
for i in str1:
    if i.isalpha():
        out_str = out_str + temp_str[cnt]
        cnt+=1
    else:
        out_str = out_str + i
print(out_str)



