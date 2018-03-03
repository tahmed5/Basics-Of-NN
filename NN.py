import numpy

def NN(m1, m2, w1, w2,b):
    z = m1 * w1 + m2 * w2 + b
    return sigmoid(z)

def sigmoid(x):
    #Returns a value from 0 to 1
    #We may have a program to generate whether a team supports Man Utd or Chelsea
    #0 may equal to Man Utd and 1 would equal to Chelsea
    print(1/(1 + numpy.exp(-x)))

w1 = numpy.random.randn()
w2 = numpy.random.randn()
b = numpy.random.randn()

NN(3,1.5,w1,w2,b)

