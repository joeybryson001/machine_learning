import math
data = [[0,1],[1,2],[2,3],[3,4],[3,6],[3.5,9]]
prediction_x_value = 5
start_m = 1
start_c = 2
acuracy_for_m = 0.00001
acuracy_for_c = 0.00001
step_size = 0.001
steps = 100000
def calculate_error(m,c,data):
    total_error_squared = 0
    for i in range(len(data)):
        estimate_y = m * data[i][0] + c
        error = data[i][1] - estimate_y
        total_error_squared += (error ** 2)
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
for i in range(steps):
    change_m,change_c = calculate_error_derivative(m,c,data)
    m = m - step_size * change_m
    c = c - step_size * change_c

print(m * prediction_x_value + c)
print(calculate_error_derivative(m,c,data))
print(m,c)



