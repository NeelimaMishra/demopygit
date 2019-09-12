'''
Write a function for checking the speed of drivers. This function should have one parameter: speed.
If speed is less than 70, it should print “Ok”.
Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point
and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
If the driver gets more than 12 points, the function should print: “License suspended”
'''
import math
import random
points = 0

def drivers_speed(speed):
    global points
    speed_limit = 70
    km = 5
    if points > 12:
        print('License suspended')
    elif speed <= speed_limit:
        print('Ok', points)
    elif speed > speed_limit:
        exceeded_speed = speed - speed_limit
        new_points = math.ceil(exceeded_speed/5)
        points = new_points + points
        print('Points: ', points)
        if points > 12:
            print('License suspended')

for i in range(0,50):
    speed = random.randint(0, 85)
    print("Passing speed: ", speed)
    drivers_speed(speed)