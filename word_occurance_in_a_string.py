s1 ="Geeksforgeeks A computer science portal for geeks  "
word = 'geeks'
s1_l = s1.split(' ')
print(s1_l)
count = 0
for i in range(len(s1_l)-1):
    if s1_l[i] == word:
        count += 1
print(count)