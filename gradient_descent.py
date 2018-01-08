import matplotlib.pyplot as plt
from numpy import *
plt.ion()
def gradient_descent_main(data_points,iterations):  
    learning_rate = 1/10000
    c_0 = 1  # initially line cuts y-axis at co-ordinate 0,1
    m_0 = -1 # initially line has gradient of -1   
    print(m_0,c_0,error_function_value(m_0,c_0,data_points))
    print("Creating Line of Best Fit iterating...")
    [c_1, m_1] = calc_gradient(data_points,c_0,m_0,learning_rate,iterations)
    print("Final")
    print(iterations,c_1,m_1,error_function_value(c_1,m_1,data_points))
def error_function_value(m,c,data_points):
    error_value = 0
    for i in range(0, len(data_points)):
        x = data_points[i, 0]
        y = data_points[i, 1]
        error_value += (y - (m * x + c)) ** 2
        final_error_value = error_value / float(len(data_points))
    return final_error_value
def calc_gradient(data_points,c_0,m_0,learning_rate,iterations):
    for i in range(iterations):
        c_1,m_1 = derive_gradients(c_0,m_0,array(data_points),learning_rate)
        #print(c_1,m_1)
    return [c_1,m_1]
def derive_gradients(c_0,m_0,data_points,learningRate):
    error_sum_c = 0
    error_sum_m = 0
    N = float(len(data_points))         
    for i in range(0, len(data_points)): 
        x = data_points[i, 0]
        y = data_points[i, 1]
        plt.scatter(x,y)
        error_sum_c += -(2/N) * (y - ((m_0 * x) + c_0))
        error_sum_m += -(2/N) * x * (y - ((m_0 * x) + c_0))
    c_1 = c_0 - (learningRate * error_sum_c)
    m_1 = m_0 - (learningRate * error_sum_m)
    #y = new_m * x + new_b
    #plt.plot(x,y)
    #plt.pause(0.05)
    for t in range(0, len(data_points)):#animating the plot
        x = data_points[t, 0]
        x_2 = 5
        y_prime = m_1 * x + c_1
        y_prime_2 = m_1 * x_2 + c_1        
        #print(x,y_prime)
        plt.scatter(x,y_prime,marker="^",color="black")        
        plt.grid(True)
        plt.pause(0.05)
    return [c_1, m_1]
data_points = genfromtxt("C:\\Users\\emenya\\Desktop\\train.csv", delimiter=",")
iterations = 5
gradient_descent_main(data_points,iterations)#beggins from here





