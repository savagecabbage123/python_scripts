import math
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
    for i in var_sample_data:
        stdev += var_sample_data[i] - mean
        stdev = stdev**2
    stdev = stdev / sample_size
    stdev = math.sqrt(stdev)
    return stdev

def pearsons_correlation_coefficient(independent_var_data: list[float], dependent_var_data: list[float]) -> float:
    """Calculates the correlation coefficient between 2 variables
    
    Args:
        independent_var_data: List containing independent variable data.
        dependent_var_data: List containing dependent variable data.

    returns:
        Correlation coefficient between 2 variables
    """

def simple_linear_regression(independent_var_data: list[float], dependent_var_data: list[float]) -> float:
    """Calculates regression coefficient and constant for linear regression.

    Args:
        independent_var_data: List containing independent variable data.
        dependent_var_data: List containing dependent variable data.

    Returns:
        m: Linear regression coefficient.
        b: Linear regression constant.
    """
    x_mean = mean_calculator(independent_var_data)
    y_mean = mean_calculator(dependent_var_data)
    x_stdev = sample_standard_deviation(independent_var_data)
    y_stdev = sample_standard_deviation(dependent_var_data)
    
    m: float = 0
    b: float = 0
    return m, b


def main():
    """Main function which runs program."""
    #TODO: data issue - make a way to import clean data easily into program

    #example input data with outputs of different functions for temporary testing
    x_data: list[float] = [1.1, 2.2, 3.2, 4.2, 5.2]
    y_data: list[float] = [1.1, 2.2, 3.2, 4.2, 5.9]
    x_mean:float = 0
    y_mean:float = 0
    x_stdev:float = 0
    y_stdev:float = 0

    x_mean = mean_calculator(x_data)
    y_mean = mean_calculator(y_data)

    print("x mean:", x_mean)
    print("y mean:", y_mean)
    
    x_stdev = sample_standard_deviation(x_data)
    y_stdev = sample_standard_deviation(y_data)

    print(x_stdev)
    print(y_stdev)
    
    #simple_linear_regression(xdata, ydata)

if __name__ == '__main__':
    main()
