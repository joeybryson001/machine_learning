from matplotlib import pyplot as plt
import math
import time
def regress(data, final_graph_complexity, starting_params, h, step_size,epsilon, iterations = None):

    def calculate_error(params, data, final_graph_complexity):
        total_error_squared = 0

        for i in range(len(data)):
            estimate_y = 0

            for l in range(final_graph_complexity):
                estimate_y += (data[i][0] ** (final_graph_complexity-1)) * params[l]

            error = data[i][1] - estimate_y
            total_error_squared += ((error) ** 2)

        return total_error_squared
    def calculate_error_derivative(params, data, h, final_graph_complexity):
        derivitives = []
        for i in range(final_graph_complexity):
            param_upper = list(params)
            param_lower = list(params) 
            param_upper[i] += h
            param_lower[i] -= h 
            derivitives.append((calculate_error(param_upper, data, final_graph_complexity) - calculate_error(param_lower, data, final_graph_complexity)) / (2 * h))
        print(derivitives[1]-derivitives[0])
        return derivitives 

    params = []

    for i in range(final_graph_complexity):
        
        if (final_graph_complexity - i - len(starting_params)) > 0:
            params.append(0)

        else:
            for i in range(len(starting_params)):
                params.append(starting_params[i])
            break
    print(params)
    print(calculate_error(params,data,final_graph_complexity))
    params[0] += 0.00001
    if not type(iterations) == int:
        while True: 
            delta = calculate_error_derivative(params, data, h)

            for l in range(final_graph_complexity):
                params[i] -= step_size * delta[l]
                finished = 0

            for i in range(final_graph_complexity):

                if params[i] < epsilon and params[i] > -epsilon:
                    finished += 1

            if finished == final_graph_complexity:
                break

    else:
        errors = []
        derivitive_history = []
        parameter_history = []
        for i in range(iterations):
            delta = calculate_error_derivative(params, data, h, final_graph_complexity)
            for l in range(final_graph_complexity):
                params[l] -= step_size * delta[l]
            errors.append(calculate_error(params,data,final_graph_complexity))
            derivitive_history.append(delta)
            parameter_history.append(params[0])
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,30))
    plt.plot(derivitive_history)
    plt.show()
    
    return params
print(regress([[1,1],[2,1],[3,1],[4,1],[5,1],[6,1]],2,[8,2],0.0001,0.000001,0.01,2000))