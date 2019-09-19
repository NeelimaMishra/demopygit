# Program to find the smallest number in a given list.

l1 = [770, 24, 2, -1, 333, 101, 50]
small_var = None
for i in l1:
    if small_var == None:
        small_var = i
        continue
    elif small_var > i:
        small_var = i
print(small_var)
