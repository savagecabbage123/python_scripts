import random
import math

# car variables
none = 0
light = 15
moderate = 25
heavy = 35
added_stop_time = 0
traffic_level = none
num_stops1 = 2 # default if no traffic for 55 mph
num_stops2 = 1 # default if no traffic for 45 mph
speed = 25
speed1 = 55 # in mph
speed2 = 45 # in mph

# generate random numbers for stopsign rng
def stopped():
    # all stop times depend on traffic level
    global num_stops1
    global num_stops2
    global added_stop_time
    global speed
    global speed1
    global speed2
    if traffic_level == none:
        num_stops1 == num_stops1
        num_stops2 == num_stops2
    elif traffic_level == light:
        stop_time = random.randrange(1,15)
        num_stops1 += 1
        num_stops2 += 1
        added_stop_time = (stop_time * (num_stops1 + num_stops2))
        if speed > 50:
            speed = 50
        if speed1 > 80:
            speed1 = 80
        if speed2 > 65:
            speed2 = 65
    elif traffic_level == moderate:
        stop_time = random.randrange(20,40)
        num_stops1 += 1
        num_stops2 += 2
        added_stop_time = (stop_time * (num_stops1 + num_stops2))
        if speed > 40:
            speed = 40
        if speed1 > 70:
            speed1 = 70
        if speed2 > 55:
            speed2 = 55
    elif traffic_level == heavy:
        stop_time = random.randrange(60,135)
        num_stops1 += 1
        num_stops2 += 3
        added_stop_time = (stop_time * (num_stops1 + num_stops2))
        if speed > 25:
            speed = 25
        if speed1 > 55:
            speed1 = 55
        if speed2 > 45:
            speed2 = 45

# calc function which calculates everything + the time for stopping from stopped function + the time added if stuck behind a vehicle
def calc():
    car_speed = speed/2.237 # converted speed in mph into m/s
    car_speed1 = speed1/2.237 # converted speed1 in mph into m/s
    car_speed2 = speed2/2.237 # converted speed 2 in mph into m/s
    car_acc = 3.13 # in m/s^2
    car2_acc = 6.26 # in m/s^2

    # stopping distance and time calculations
    # both cars for speed
    car1_stop_time = ((speed*1.467)/15) + 1
    car2_stop_time = ((speed*1.467)/20) + 1
    car1_stop_dist = ((.5*speed)*(car1_stop_time))/3.281
    car2_stop_dist = ((.5*speed)*(car2_stop_time))/3.281
    # both cars for speed1
    car1_stop_time1 = ((speed1*1.467)/15) + 1
    car2_stop_time1 = ((speed1*1.467)/20) + 1
    car1_stop_dist1 = ((.5*speed1)*(car1_stop_time1))/3.281
    car2_stop_dist1 = ((.5*speed1)*(car2_stop_time1))/3.281
    # both cars for speed2
    car1_stop_time2 = ((speed2*1.467)/15) + 1
    car2_stop_time2 = ((speed2*1.467)/20) + 1
    car1_stop_dist2 = ((.5*speed2)*(car1_stop_time1))/3.281
    car2_stop_dist2 = ((.5*speed2)*(car2_stop_time1))/3.281

    # distance to travel
    Mile_distance = .6 # distance in miles for speed of 25 mph
    Mile_distance1 = 8.5 # distance in miles for speed of 55 mph
    Mile_distance2 = 2.7 # distance in miles for speed of 45 mph
    Distance = Mile_distance*1609.34 # distance in meters for speed of 25 mph
    Distance1 = Mile_distance1*1609.34 # distance in meters for speed of 55 mph
    Distance2 = Mile_distance2*1609.34 # distance in meters for speed of 45 mph

    # acceleration distance calculations
    car_acc_distance = (car_speed ** 2) / (2 * car_acc)
    car2_acc_distance = (car_speed ** 2) / (2 * car2_acc)

    car_acc_distance1 = (car_speed1 ** 2) / (2 * car_acc)
    car_acc_distance2 = (car_speed2 ** 2) / (2 * car_acc)

    car2_acc_distance1 = (car_speed1 ** 2) / (2 * car2_acc)
    car2_acc_distance2 = (car_speed2 ** 2) / (2 * car2_acc)

    # time calculations
    car_acc_time = math.sqrt((2 * car_acc_distance)/car_acc)
    car2_acc_time = math.sqrt((2 * car2_acc_distance)/car_acc)

    car_acc_time1 = math.sqrt((2 * car_acc_distance1)/car_acc)
    car_acc_time2 = math.sqrt((2 * car_acc_distance2)/car_acc)

    car2_acc_time1 = math.sqrt((2 * car2_acc_distance1)/car2_acc)
    car2_acc_time2 = math.sqrt((2 * car2_acc_distance2)/car2_acc)

    # total time calc
    car1_time = ((((Distance)/speed) + 7) + ((Distance1 - (num_stops1 * car_acc_distance1))/car_speed1 + (Distance2 - (num_stops2 * car_acc_distance2))/car_speed2) + ((num_stops1 * car_acc_time1) + (num_stops2 * car_acc_time2)) + added_stop_time)/60
    car2_time = ((((Distance)/speed) + 7) + ((Distance1 - (num_stops1 * car2_acc_distance1))/car_speed1 + (Distance2 - (num_stops2 * car2_acc_distance2))/car_speed2) + ((num_stops1 * car2_acc_time1) + (num_stops2 * car2_acc_time2)) + added_stop_time)/60
    # divmod returns both quotient and remainder so in this case, it takes the time that is calculated and instead of having a long decimal
    # on the end of the minutes, it seperates that decimal as the remainder and then in the print function, I convert the decimal into time in seconds
    min, sec = divmod(car1_time, 1)
    min1, sec1 = divmod(car2_time, 1)
    print("the first car took", round(min), "minutes, and", round(sec*60), "seconds")
    print("the second car took", round(min1), "minutes, and", round(sec1*60), "seconds")

# generate rng for being pulled over if you are going 5 miles per hour over the speed limit or more except in neighborhood there is no exception
def arrested():
    print("you have been pulled over...")
    print("you did not make it to school")
    exit()
def pulledover():
    if speed > 25:
        chance = random.randrange(1, 1501)
        if chance > 1 and chance < 2:
            arrested()
    elif speed1 > 60 and speed1 <= 80:
        chance = random.randrange(1, 1501)
        if chance >= 300 and chance <= 389:
            arrested()
    elif speed1 >= 80:
        chance = random.randrange(1, 6)
        if chance == 1:
            arrested()
    elif speed2 > 50 and speed2 <= 70:
        chance = random.randrange(1, 1260)
        if chance >= 130 and chance <= 230:
            arrested()
    elif speed2 > 70:
        chance = random.randrange(1, 4)
        if chance == 1:
            arrested()

# run functions
for i in range(1):
    #print("attempt", i + 1)
    pulledover()
    stopped()
    calc()