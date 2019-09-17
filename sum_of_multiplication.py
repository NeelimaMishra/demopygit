'''
Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
'''

def sum_of_multiples(limit):


        sum = 0
        for num in range(0, limit + 1):
            if num % 3 == 0 or num % 5 == 0:
                sum += num
        print(sum)
sum_of_multiples(20)