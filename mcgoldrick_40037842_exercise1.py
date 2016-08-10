import numpy as np
import matplotlib.pyplot as plt

piarray3 = np.zeros([20])
#Defines an empty array where pi values will be recorded.
def pi(i):
#Defines a new function to obtain values of pi.
    for i in np.arange(1,20):
#Establishes a loop counting each integer from 1 to 20.
        X = np.random.uniform(low=-1,high=1,size=20000)
        Y = np.random.uniform(low=-1,high=1,size=20000)
#Note the value size is 5000 for 2f and 20000 for 2g.
        Xsq = np.power(X,2)
        Ysq = np.power(Y,2)
        sumsq = Xsq + Ysq
        radius = np.sqrt(sumsq)
        good = radius <= 1.0
#Everything is the same inside the loop as before.
        piarray3[i]=4*(np.float(good.sum())/np.float(len(radius)))
#We now store the Pi values in our empty array instead of printing.
        i = i + 1
#We move to the next iteration of the array.
        
print pi(0)
#This simply prompts the function pi(i) to begin.

print "Mean is:"
print np.mean(piarray3)
print "Standard Deviation is:"
print np.std(piarray3)
#A mean and stan. deviation is given for the array of pi-values.
