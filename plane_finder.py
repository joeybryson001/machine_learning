def calculate_differential(data,m,c):
    error1 = calculate_differential(m + acuracy,c,data)
    error2 = calculate_differential(m + acuracy * ((3 ** (1 / 2)),c - acuracy * ((3 ** (1 / 2))),data)
    error3 = calculate_differential(m - acuracy * ((3 ** (1 / 2)),c - acuracy * ((3 ** (1 / 2))),data)


    print("iterations:"+str(counter))
    print("time taken:"+str(time.time() - start_time))
    print("final error is:"+str(calculate_error_derivative(m,c,data)))
    if c > 0:
        print("equation of final line is:y = "+str(m)+"X + "+str(c))
    else:
        print("equation of final line is:y = "+str(m)+"X "+str(c))