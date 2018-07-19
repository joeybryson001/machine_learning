"""parameters for this function: data - 2D list,parameters - list, h - small float or int, step_size - small float or int,
epsilon - small float or int, iterations(optional) - default is None otherwise int""" 
from matplotlib import pyplot
import math
import time
def regress(data,parameters,h,step_size,epsilon,iterations = 100):
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
                estimate_y += (data[i][0] ** (len(parameters)-l-1)) * parameters[l]
            error = data[i][1] - estimate_y
            total_error_squared += ((error) ** 2)
        return total_error_squared
    #differential function used to calculate the dirivitive;
    def calculate_error_derivative(parameters,data,h):
        derivitives = []
        for i in range(len(parameters)):
            param_upper = list(parameters)
            param_lower = list(parameters) 
            param_upper[i] += h
            param_lower[i] -= h 
            derivitives.append((calculate_error(param_upper,data)-calculate_error(param_lower,data))/(2 * h))

        return derivitives 
    #setting variables;
    counter = 0
    counter2 = 0
    errors = []
    dirivitive_history = []
    parameter_history = []
    #while loop impliments changes to m and c until dirivitive is within an acceptable_error;
    if not type(iterations) == int:
        while not (1 == 1): 
            for i in range(parameters):
                delta = calculate_error_derivative(parameters,data,h)
                parameters[i] -= step_size * delta
            counter += 1  
    else:
        for i in range(iterations):
            delta = calculate_error_derivative(parameters,data,h)
            for l in range(len(parameters)):
                parameters[l] -= step_size * delta[l]
                counter +=1
            counter2 +=1
            errors.append(calculate_error(parameters,data))
            dirivitive_history.append(calculate_error_derivative(parameters,data,h))
            parameter_history.append(parameters[0])
    pyplot.ticklabel_format(style='sci', axis='y', scilimits=(0,30))
    pyplot.plot(dirivitive_history)
    pyplot.show()


    print(counter,counter2)
    #results and info about program's performence;
    return parameters
print(regress([[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]],[8,2],0.00001,0.000001,0.01,2000))
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
