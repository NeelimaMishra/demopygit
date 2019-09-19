l1 = [9, 12, 6, 4, 87]
max_no = None
for i in l1:
    if max_no == None:
        max_no = i
        continue
    elif max_no < i:
        max_no = i
print(max_no)