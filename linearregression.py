import numpy
import time

def get_coordinates():
    global x_coord
    global y_coord
    x_coord = []
    y_coord = []
    entering_coordinates = True
    print('Enter Your x and y Coordinates in the format x,y')
    print("Type 'done' when you are finished")
    while entering_coordinates == True:
        data = input()
        if data == 'done':
            if len(x_coord) < 2 or len(y_coord) < 2:
                print('not enough data inputted')
                exit()
            entering_coordinates = False
            break          
        data = data.split(',')
        if len(data) != 2:
            print("Invalid Format: E.G x,y --> 5,3")
            continue
        if data[0] == '' or data[1] == '':
            print('Incomplete coorindates')
            continue
        try:
            data[0] = int(data[0])
            data[1] = int(data[1])
        except:
            print('String Detected')
            continue 
        x_coord.append(data[0])
        y_coord.append(data[1])
        
def partial_derivative_m(m,c):
    sum_gradient_m = 0
    for x in range(len(x_coord)):
        sum_gradient_m +=  (2 *  x_coord[x]) * (m * x_coord[x] + c - y_coord[x])
    return 1/len(x_coord) * sum_gradient_m
        
def partial_derivative_c(m,c):
    sum_gradient_c = 0
    for x in range(len(x_coord)):
        sum_gradient_c +=  2 * (m * x_coord[x] + c - y_coord[x])
    return 1/len(x_coord) * sum_gradient_c
               
    

def main():
    get_coordinates()
    c = 1
    m = 1
    while True:
        m = m - 0.01 * partial_derivative_m(m,c)
        c = c - 0.01 * partial_derivative_c(m,c)
        print('M:', m)
        print('C:', c)
        
        
            


main()
