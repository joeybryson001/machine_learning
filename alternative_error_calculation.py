def calculate_error(m,c,data):
    total_error_squared = 0
    for i in range(len(data)):
        y_intercept = data[i][1] + (data[i][0] / m)
        x_of_closest_point = (y_intercept - c) / (m - ((-1) / m))
        y_of_closest_point = m * x_of_closest_point + c
        error = math.sqrt(((x_of_closest_point - data[i][0]) ** 2) + ((y_of_closest_point - data[i][1]) ** 2))
        total_error_squared += error ** 2
    return total_error_squared