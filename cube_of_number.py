#write a code to find the cube of a number.Take the input from user using input() and also using command line.

#num =  int(input('Enter a integer number: '))
import sys
num = int(sys.argv[1])
cube_num = num ** 3
print(cube_num)

'''
from cmd run this program like this
D:\pythonPrograms>python "program using sys module".py 2
8
'''