import math
import time
start_time = time.time()
data = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[100000000000000,-90000000000000]]
prediction_x_value = 90
start_m = -100
start_c = -20
acuracy_for_m = 0.00001
acuracy_for_c = 0.00001
step_size = 0.01
acceptible_error = 0.1
def calculate_error(m,c,data):
    total_error_squared = 0
    for i in range(len(data)):
        estimate_y = m * data[i][0] + c
        error = data[i][1] - estimate_y
        total_error_squared += (error ** 2)
    return total_error_squared
def calculate_error_2(m,c,data):
    total_error_squared = 0
    for i in range(len(data)):
        y_intercept = data[i][1] + (data[i][0] / m)
        x_of_closest_point = (y_intercept - c) / (m - ((-1) / m))
        y_of_closest_point = m * x_of_closest_point + c
        error = math.sqrt(((x_of_closest_point - data[i][0]) ** 2) + ((y_of_closest_point - data[i][1]) ** 2))
        total_error_squared += error ** 2
    return total_error_squared
def calculate_error_derivative(m,c,data):
    c_derivative1 = calculate_error(m,c - acuracy_for_c,data) 
    c_derivative2 = calculate_error(m,c + acuracy_for_c,data)
    c_derivative = (c_derivative1 - c_derivative2) / (-2 * acuracy_for_c)
    m_derivative1 = calculate_error(m - acuracy_for_m,c,data) 
    m_derivative2 = calculate_error(m + acuracy_for_m,c,data)
    m_derivative = (m_derivative1 - m_derivative2) / (-2 * acuracy_for_m)
    return m_derivative, c_derivative   
m = start_m
c = start_c
change_m, change_c = calculate_error_derivative(m,c,data)
while change_c + change_m > acceptible_error:
    change_m,change_c = calculate_error_derivative(m,c,data)
    m = m - step_size * change_m
    c = c - step_size * change_c
print("time taken:"+str(time.time() - start_time))
print("prediction for x = "+str(prediction_x_value)+" is "+str(m * prediction_x_value + c))
print("final error is:"+str(calculate_error_derivative(m,c,data)))
print("equation of final line is:y = "+str(m)+"X + "+str(c))



