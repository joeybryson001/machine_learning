"""parameters for this function: data - 2D list,parameters - list, h - small float or int, step_size - small float or int,
epsilon - small float or int, iterations(optional) - default is None otherwise int""" 
def regress(data,parameters,h,step_size,epsilon,iterations = None):
    import math
    import time
    start_time = time.time()
    #checking for invalid input
    if not type(data) == list:
        print("wrong data type for 'data'")
        return
    if not type(parameters) == list:
        print("wrong data type for 'parameters'")
        return
    if not (type(h) == int or type(h) == float):
        print("wrong data type for 'h'")
        return
    if not (type(step_size) == int or type(step_size) == float):
        print("wrong data typefor 'step_size'")
        return
    if not (type(epsilon) == int or type(step_size) == float):
        print("wrong data type for 'epsilon'")
        return
    if not (type(iterations) == int or iterations is None):
        print("wrong data type for 'iterations'")
        return

    #sum of squares function used to calculate error;
    def calculate_error(parameters,data):
        total_error_squared = 0
        for i in range(len(data)):
            estimate_y = 0
            for l in range(len(parameters)):
                estimate_y += data[i][0]**(len(parameters)-l) * parameters[l]
                
            error = data[i][1] - estimate_y
            total_error_squared += (error ** 2)
        return total_error_squared
    print(calculate_error([1,1],[[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]]))
    #differential function used to calculate the dirivitive;
    def calculate_error_derivative(m,c,data):
        c_derivative = (calculate_error(m,c - h,data) - calculate_error(m,c + h,data)) / (-2 * h)
        m_derivative = (calculate_error(m - h,c,data) - calculate_error(m + h,c,data)) / (-2 * h)
        return m_derivative, c_derivative 
    #setting variables;
    m = parameters[0]
    c = parameters[1]
    delta_m, delta_c = calculate_error_derivative(m,c,data)
    counter = 0
    #while loop impliments changes to m and c until dirivitive is within an acceptable_error;
    if not type(iterations) == int:
        while not (delta_m < epsilon and delta_m > -epsilon and delta_c < epsilon and delta_c > -epsilon): 
            delta_m,delta_c = calculate_error_derivative(m,c,data)
            m = m - step_size * delta_m
            c = c - step_size * delta_c
            counter += 1  
    else:
        for i in range(fixed_length):
            change_m,change_c = calculate_error_derivative(m,c,data)
            m = m - step_size * change_m
            c = c - step_size * change_c

    #results and info about program's performence;
    final_values = [m,c]
    return final_values
def predict(x,parameters):
        if not( type(parameters) == list):
            print("wrong data type for 'parameters'")
            return
        if not (type(x) == int or type(x) == float):
            print("wrong data type for 'x'")
            return
        y = parameters[0]*x + parameters[1]
        return y
#example;
print(predict(10,regress([[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]],[1,1],0.001,0.001,0.00000001)))