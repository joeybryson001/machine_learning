import unittest
import math
import time
start_time = time.time()
#put your data hear as a 2D list;
data = [[0,-10000],[1,-2],[2,3],[3,4],[4,5],[5,600]]
#set these variables to suit your list;
start_m = -100
start_c = -20
acuracy_for_m = 0.001
acuracy_for_c = 0.001
step_size = 0.1
acceptable_error_c = 0.00000001
acceptable_error_m = 0.00000001
#sum of squares function used to calculate error;
def calculate_error(m,c,data):
    total_error_squared = 0
    for i in range(len(data)):
        total_error_squared += (data[i][1] - (m * data[i][0] + c)) ** 2
    return total_error_squared
#differential function used to calculate the dirivitive;
def calculate_error_derivative(m,c,data):
    c_derivative = (calculate_error(m,c - acuracy_for_c,data) - calculate_error(m,c + acuracy_for_c,data)) / (-2 * acuracy_for_c)
    m_derivative = (calculate_error(m - acuracy_for_m,c,data) - calculate_error(m + acuracy_for_m,c,data)) / (-2 * acuracy_for_m)
    return m_derivative, c_derivative 
#setting variables;
m = start_m
c = start_c
change_m, change_c = calculate_error_derivative(m,c,data)
counter = 0
#while loop impliments changes to m and c until dirivitive is within an acceptable_error;
while not (change_m < acceptable_error_m and change_m > -acceptable_error_m and change_c < acceptable_error_c and change_c > -acceptable_error_c): 
    change_m,change_c = calculate_error_derivative(m,c,data)
    m = m - step_size * change_m
    c = c - step_size * change_c
    counter += 1
    if counter > 100000:
        print("timed out")
        break  
#results and info about program's performence;
print("iterations:"+str(counter))
print("time taken:"+str(time.time() - start_time))
print("final error is:"+str(calculate_error_derivative(m,c,data)))
if c > 0:
    print("equation of final line is:y = "+str(m)+"X +"+str(c))
else:
    print("equation of final line is:y = "+str(m)+"X "+str(c))
