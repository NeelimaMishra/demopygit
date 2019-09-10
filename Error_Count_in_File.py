fd = open('C:/Users/neelima.mishra/Desktop/error_cnt.txt', 'r')
lines = fd.readlines()
print(lines)
error_line = 1 #line number
for i in lines: # here i is one element in the list
    if 'error' in i:
        error_count = len(i.split('error')) -1 # this is the error count in each line
        print('errors: LineNumber{} Count{}'.format(error_line, error_count))
    error_line += 1

