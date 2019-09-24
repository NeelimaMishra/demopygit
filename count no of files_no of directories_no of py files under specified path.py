import os
#print(os.walk("D:\\Test"))
'''
>>> for obj in os.walk("D:\\Test"):
...     print(obj)
...
('D:\\Test', ['New folder'], ['file Outside New folder.txt'])
('D:\\Test\\New folder', ['Inside New folder - new dir'], ['Inside New folder - new file.txt'])
('D:\\Test\\New folder\\Inside New folder - new dir', [], [])
'''
cnt = 1
for i in os.walk("D:\\Test"):
    if i[0] == "D:\\Test":
        dir_cnt = len(i[1])
        file_cnt = len(i[2])
        for file in i[2]:
            ext = file.split('.')[-1]                    #for ext in i[2].split('.')[-1]:
            if ext == '.txt':
                cnt += 1
        print('Txt file count is: ', cnt)
print('Directory count is: ', dir_cnt)
print('File count is: ', file_cnt)
