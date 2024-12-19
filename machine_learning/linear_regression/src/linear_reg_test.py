"""Simple testing file.

For now I just have test cases that I manually tried which worked.
"""

import numpy as np
import linear_regression as lr

def run_test(test_name: str, test_val: float, expected_val: float):
    """Runs the test and determines pass or fail.

    Args:
        test_name: The name of the test that passed or failed.
        test_val: The value that was calculated and is checked against.
        expected_val: The expected value.
    
    Returns:
        Nothing.
    """
    #maybe use assert
    if (abs(test_val - expected_val) <= .1):
        print(f"Test {test_name}: PASSED")
    else:
        print(f"Test {test_name}: FAILED")
        print(f"actual: {test_val}, expected: {expected_val}")

#TODO: data generation - make a way to generate clean random data for proper test

#simple linear regression testing

#test 1 data
x_data: list[float] = [17, 13, 12, 15, 16, 14, 16, 16, 18, 19]
y_data: list[float] = [94, 73, 59, 80, 93, 85, 66, 79, 77, 91]

#test 1 expected results
x_mean_expected: float = 15.6
y_mean_expected: float = 79.7
x_stdev_expected: float = 2.17
y_stdev_expected: float = 11.576
r_expected: float = .596
m_expected: float = 3.179
b_expected: float = 30.104

x_mean: float = lr.mean_calculator(x_data)
y_mean: float = lr.mean_calculator(y_data)
run_test("xmean", x_mean, x_mean_expected)
run_test("ymean", y_mean, y_mean_expected)

x_stdev: float = lr.sample_standard_deviation(x_data, x_mean)
y_stdev: float = lr.sample_standard_deviation(y_data, y_mean)
run_test("xstdev", x_stdev, x_stdev_expected)
run_test("ystdev", y_stdev, y_stdev_expected)

r_test = lr.pearsons_correlation_coefficient(x_data, y_data, x_mean_expected, y_mean_expected)
run_test("r", r_test, r_expected)

#test 2 data
x_data: list[float] = [1, 2, 3, 4, 5, 6]
y_data: list[float] = [2, 4, 7, 9, 12, 14]

#test 2 expected results
x_mean_expected: float = 3.5
y_mean_expected: float = 8
x_stdev_expected: float = 1.87
y_stdev_expected: float = 4.60
r_expected = .998

x_mean: float = lr.mean_calculator(x_data)
y_mean: float = lr.mean_calculator(y_data)
run_test("xmean", x_mean, x_mean_expected)
run_test("ymean", y_mean, y_mean_expected)

x_stdev: float = lr.sample_standard_deviation(x_data, x_mean)
y_stdev: float = lr.sample_standard_deviation(y_data, y_mean)
run_test("xstdev", x_stdev, x_stdev_expected)
run_test("ystdev", y_stdev, y_stdev_expected)

r_test = lr.pearsons_correlation_coefficient(x_data, y_data, x_mean_expected, y_mean_expected)
run_test("r", r_test, r_expected)

"""
#test 3 data
x_data: list[float] = []
y_data: list[float] = []

#test 3 expected results
x_mean:float = 
y_mean:float = 
x_stdev:float = 
y_stdev:float = 
r = 

x_mean: float = lr.mean_calculator(x_data)
y_mean: float = lr.mean_calculator(y_data)
run_test("xmean", x_mean, x_mean_expected)
run_test("ymean", y_mean, y_mean_expected)

x_stdev: float = lr.sample_standard_deviation(x_data, x_mean)
y_stdev: float = lr.sample_standard_deviation(y_data, y_mean)
run_test("xstdev", x_stdev, x_stdev_expected)
run_test("ystdev", y_stdev, y_stdev_expected)

r_test = lr.pearsons_correlation_coefficient(x_data, y_data, x_mean_expected, y_mean_expected)
run_test("r", r_test, r_expected)
"""

#test 3 data
#x0 = [1, 1, 1], x1 = [-1, 1, 2], B0 and B1 relate to x0 and x1 respectively
#for y = B0 + x1B1
x = np.array([[1, -1], [1, 1], [1, 2]])
y = np.array([-2, 0, 3])

#test 3 expected results
b = [-.71, 1.57]

b_result = lr.ordinary_least_squares(x, y)
run_test("B0", b[0], b_result[0])
run_test("B1", b[1], b_result[1])
