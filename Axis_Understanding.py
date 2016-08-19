import numpy as np
a = np.reshape(np.arange(9),(3,3))
print a
print "Axis 0 Sum:" ,np.sum(a,axis = 0) #Adds the element vertically
print "Axis 1 Sum: ",np.sum(a,axis = 1) #Adds the element horizontally
b = np.arange(3)
print b.shape
print a + b
b = b[:,np.newaxis] #changes the dimension of b from 1D to 2D
print b.shape
print b 

