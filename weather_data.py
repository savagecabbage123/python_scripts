# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         zachary lawrence
# Section:      516
# Assignment:   lab 11b
# Date:         11/7/2022
#

import csv

dict_months = {"January": "1", "February": "2", "March": "3", "April": "4", "May": "5", "June": "6", "July": "7", "August": "8", "September": "9", "October": "10", "November": "11", "December": "12",}

with open('WeatherDataCLL.csv', 'r') as csvfile:
    #reads csv file
    data_reader = csv.reader(csvfile, delimiter=',')
    row_num = 0
    max_num = 0
    min_num = 100

    #precipitation average
    p_avg = 0

    for row in data_reader:
        #not the title row then compare temp values as well as add up precipation for average
        if row_num > 1:
            if max_num < int(row[4]):
                max_num = int(row[4])
            if min_num > int(row[5]):
                min_num = int(row[5])
            p_avg += float(row[2])
        row_num += 1
    p_avg /= row_num

    print(f"3-year maximum temperature: {max_num} F")
    print(f"3-year minimum temperature: {min_num} F")
    print(f"3-year average precipitation: {p_avg:.3f} inches")

with open('WeatherDataCLL.csv', 'r') as csvfile:
    data_reader = csv.reader(csvfile, delimiter=',')
    month = input("Please enter a month: ")
    year = input("Please enter a year: ")
    print(f"For {month} {year}:")
    month = dict_months.get(month)
    temp_avg = 0
    wind_avg = 0
    #precipitation percent
    p_perc = 0
    days = 0
    row_num = 0

    for row in data_reader:
        #maybe call a split function
        if row_num != 0:
            data = row[0].split("/")
            if month == data[0] and year == data[2]:
                temp_avg += float(row[4])
                wind_avg += float(row[1])
                if row[2] != "0":
                    p_perc += 1
                days += 1
        row_num += 1
    
    temp_avg /= days
    wind_avg /= days
    p_perc /= days
    print(f"Mean maximum daily temperature: {temp_avg:.1f} F")
    print(f"Mean daily wind speed: {wind_avg:.2f} mph")
    print(f"Percentage of days with precipitation: {p_perc*100:.1f}%")
    