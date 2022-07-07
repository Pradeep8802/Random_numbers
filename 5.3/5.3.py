#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

simlen = int(1e6)
var_Y= np.loadtxt('Var_Y.dat', dtype='double')
x = np.linspace(0, 1, simlen)
plt.plot(x, var_Y, '.')
plt.xlabel('n ($\\times 10^6$)')
plt.ylabel('y(n)')
plt.grid()
plt.show()