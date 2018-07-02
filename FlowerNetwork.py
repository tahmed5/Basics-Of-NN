from matplotlib import pyplot as plt
import numpy as np
import os 

#length,width,colour 1 = red 0 = blue
data = [[3,1.5,1],
        [2,1,0],
        [4,1.5,1],
        [3,1,0],
        [3.5, 0.5,1],
        [2,0.5,0],
        [5.5,1,1],
        [1,1,0]]

mystery_flower = [4.5, 1]

#network

#    o   flower type
#   / \  w1,w2,b
#  o   o length,width

w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()

# return a value between 0 and 1. When x -> inf ans -> 0. When x -> -inf ans -> 1. 
def sigmoid(x):
    return 1/(1 + np.exp(-x))

# takes the derivative of sigmoid
def sigmoid_p(x):
    return sigmoid(x) * (1- sigmoid(x))

X = np.linspace(-5, 5, 100) #generates 100 points between -5 and 5
Y = sigmoid(X) # applies sigmoid to all the points in the array X
#plt.plot(X,Y) # plots x by y
#plt.show() # used to display the plot on idle 

# scatter data
for i in range(len(data)):
    point = data[i]
    colour = "r"
    if point[2] == 0:
        colour = "b"
#    plt.scatter(point[0], point[1], c = colour)
#plt.show()

#training loop
learning_rate = 0.2
costs = []

for i in range(100000):
    ri = np.random.randint(len(data)) #takes a random index
    point = data[ri] #selects the data point at that random index 

    z = point[0] * w1 + point[1] * w2 + b #applies the weights to our points
    pred = sigmoid(z) #the sigmoid of z is taken to give us a prediction

    target = point[2] #our target is the actual value so either blue or red (0 , 1)
    cost = np.square((pred - target)) #(pred-target) ** 2 is our cost squared function to show how far we were from the true value
    costs.append(cost)
        
    dcost_pred = 2* (pred - target) #derivative of cost function to give us the gradient function
    dpred_dz = sigmoid_p(z) #derivative of sigmoid and z is passed in
    
    dz_dw1 = point[0] #when finding the derviative rom our z point dz/dw1 = point[0]
    dz_dw2 = point[1] #when finding the derviative rom our z point dz/dw2 = point[1]
    dz_db = 1 # b^1 dz/db = 1

    dcost_dz = dcost_pred * dpred_dz

    #partial derivatives
    dcost_dw1 = dcost_dz * dz_dw1 #taking derivative the cost of our prediction and multiplynig it with the derivative of our prediction with the deriviative of our weight to give us our cost relative to the other derivatives.
    dcost_dw2 = dcost_dz * dz_dw2
    dcost_db = dcost_dz * dz_db

    w1 = w1 - learning_rate * dcost_dw1 #learning rate is our alpha value control what percentage of dcost we shou;d to use to adjust our weights
    w2 = w2 - learning_rate * dcost_dw2
    b = b - learning_rate * dcost_db


plt.plot(costs)
plt.show()

#seeing model predictions
for i in range(len(data)):
    point = data[i]
    print(point)
    z = point[0] * w1 + point[1] * w2 + b
    pred = sigmoid(z)
    print("pred: {}".format(pred))

z = mystery_flower[0] * w1 + mystery_flower[1] * w2 +b
pred = sigmoid(z)
con_colour = round(pred,1)
print(con_colour)
if con_colour == 0:
    print('Colour is Blue')
if con_colour == 1:
    print('Colour is Red')

def which_flower(length,width):
    z = length * w1 + width * w2 + b
    pred = sigmoid(z)
    if con_colour == 0:
        os.system("say blue")
    if con_colour == 1:
        os.system("say red")
    
which_flower(1,1)
