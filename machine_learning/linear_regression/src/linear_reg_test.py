"""Simple testing file.

For now I just have test cases that I manually tried which worked.
"""

#TODO: testing - make a way to auto test my program when this file runs
#TODO: data generation - make a way to generate clean random data for proper test

#test 1 data
x_data: list[float] = [17, 13, 12, 15, 16, 14, 16, 16, 18, 19]
y_data: list[float] = [94, 73, 59, 80, 93, 85, 66, 79, 77, 91]

#test 1 expected results
x_mean:float = 15.6
y_mean:float = 79.7
x_stdev:float = 2.17
y_stdev:float = 11.576
r = .596

#test 2 data
x_data: list[float] = [1, 2, 3, 4, 5, 6]
y_data: list[float] = [2, 4, 7, 9, 12, 14]

#test 2 expected results
x_mean:float = 3.5
y_mean:float = 8
x_stdev:float = 1.87
y_stdev:float = 4.60
r = .998