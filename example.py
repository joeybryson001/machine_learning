"""
    It computes the Sum of Squared Errors between the 
    given data and the given hypothesis.

    The function expects the data to be a list of
    points in the form [[x_1, y_1], [x_2, y_2], ...]
    and the hypothesis to be a list of values
    of the same length as the number of points in data
    representing the 'guesses' made by a predictor/regressor
    for each x in the data points.

    It computes sum(y_i - y_hat_i)^2

"""
def sum_square_error(data, hypothesis):
    if not data and not hypothesis:
        return None
    return -1




