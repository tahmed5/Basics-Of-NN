
#This is our squared error used to figure out how far we were from our target value
#(prediction - target) ** 2

def cost(b):
    return (b-4) ** 2

#Calculus by first derivative giving a gradient function which we can use to find out whether to increment or decrement b to get to our target value
#dy/dx
#Downfall is that it calls cost twice

def num_slope(b):
    h = 0.0001
    return (cost(b+h) - cost(b))/h

#By using the power rule we can derive this gradient function
def slope(b):
    return 2 * (b-4)

b = 8

while True: 
    b = b - 0.1 * slope(b)
    print(b)
