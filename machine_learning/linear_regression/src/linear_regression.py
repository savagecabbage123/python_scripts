import math
import numpy as np
"""This program will be used to calculate linear regression from scratch.

I will be implementing the calculations for linear regression using a variety
of different methods which include:
1. Simple Linear Regression
2. Ordinary Least Squares
3. Gradient Descent

More methods may be added above later.
"""

def mean_calculator(var_data: list[float]) -> float:
    """Calculates the mean of a set of data.

    Args:
        var_data: List containing data regarding a variable.

    returns:
        The mean of the set of data.
    """
    mean: float = 0
    for val in var_data:
        mean += val
    return mean / len(var_data)

def sample_standard_deviation(var_sample_data: list[float], mean: float) -> float:
    """Calculates the standard deviation of a sample set of data.

    Args:
        var_sample_data: List containing sample of population data.

    Returns:
        The sample standard deviation of a dataset.
    """
    sample_size = len(var_sample_data) - 1
    stdev = 0
    for var_data in var_sample_data:
        sum = var_data - mean
        stdev += sum**2 / sample_size
    #stdev = stdev / sample_size
    stdev = math.sqrt(stdev)
    return stdev

def pearsons_correlation_coefficient(independent_var_data: list[float], 
                                     dependent_var_data: list[float], 
                                     independent_mean, dependent_mean
                                     ) -> float:
    """Calculates the correlation coefficient between 2 variables.
    
    Args:
        independent_var_data: List containing independent variable data.
        dependent_var_data: List containing dependent variable data.
        independent_mean: Independent variable mean value.
        dependent_mean: Dependent variable mean value.

    returns:
        Correlation coefficient between 2 variables.
    """

    top_sum = 0
    bottom_left_sum = 0
    bottom_right_sum = 0
    for i in range(len(independent_var_data)):
        sum_x = independent_var_data[i] - independent_mean
        sum_y = dependent_var_data[i] - dependent_mean
        top_sum += sum_x * sum_y
        bottom_left_sum += sum_x**2
        bottom_right_sum += sum_y**2
    bottom_sum = math.sqrt(bottom_left_sum * bottom_right_sum)
    correlation = top_sum / bottom_sum
    return correlation


def simple_linear_regression(independent_var_data: list[float], 
                             dependent_var_data: list[float]
                             ) -> float:
    """Calculates regression coefficient and constant for linear regression.

    Args:
        independent_var_data: List containing independent variable data.
        dependent_var_data: List containing dependent variable data.

    Returns:
        m: Linear regression coefficient.
        b: Linear regression constant.
    """
    x_mean: float = mean_calculator(independent_var_data)
    y_mean: float = mean_calculator(dependent_var_data)
    r = pearsons_correlation_coefficient(independent_var_data, 
                                         dependent_var_data, 
                                         x_mean, 
                                         y_mean
                                         )

    if (abs(r) < .5):
        print("Linear regression cannot be used to predict values from this data")
        return 0, 0
    
    x_stdev: float = sample_standard_deviation(independent_var_data, x_mean)
    y_stdev: float = sample_standard_deviation(dependent_var_data, y_mean)
    
    m: float = r * (y_stdev / x_stdev)
    b: float = y_mean - m * x_mean
    return m, b

def ordinary_least_squares(independent_matrix: list[list[float]],
                           dependent_matrix: list[float]
                           ) -> list[float]:
    """Calculates the coefficient matrix for one or more independent variables.
    
    Args:
        independent_matrix: Matrix of independent variables with corresponding data.
        dependent_matrix: Matrix containing dependent variable data.

    Returns:
        B: Matrix of linear regression coefficients.
    """
    return


def main():
    """Main function which runs program."""
    #TODO: data issue - make a way to import clean data easily into program

    #example input data with outputs of different functions for temporary testing
    x_data: list[float] = [1, 8, 10, 22]
    y_data: list[float] = [9, 1, 3, 11]
    x_mean:float = 0
    y_mean:float = 0
    x_stdev:float = 0
    y_stdev:float = 0

    x_mean = mean_calculator(x_data)
    y_mean = mean_calculator(y_data)

    print("x mean: ", x_mean)
    print("y mean: ", y_mean)
    
    x_stdev = sample_standard_deviation(x_data, x_mean)
    y_stdev = sample_standard_deviation(y_data, y_mean)

    print("x sample standard deviation: ", x_stdev)
    print("y sample standard deviation: ", y_stdev)
    #simple_linear_regression(xdata, ydata)

    r = pearsons_correlation_coefficient(x_data, y_data, x_mean, y_mean)
    print("Correlation coefficient: ", r)

    m, b = simple_linear_regression(x_data, y_data)
    print(f"y = {m}x + {b}")

if __name__ == '__main__':
    main()
