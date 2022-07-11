import matplotlib.pyplot as plt
import numpy as np
import math 
import scipy

# Q function
def Q(x):
    return (math.erfc(x/math.sqrt(2)))/2

# The theoritical cdf    
def F(x):
    return 1-Q(x)

A=5# given

# Pe_del is a function which returns 
def Pe_del(x):
    a=1-F(5+x)+F(-5+x)
    return a/2

x=np.linspace(-20,20,1000)
	
vect_cdf = scipy.vectorize(Pe_del)
plt.plot(x,vect_cdf(x),color='orange') # Theoretical
plt.xlabel("$delta$")
plt.ylabel("$P_e$")
plt.grid()
plt.show()
