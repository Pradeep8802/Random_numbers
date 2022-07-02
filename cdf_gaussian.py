#Importing numpy, scipy, mpmath and pyplot
from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import math as m
import mpmath
import scipy
def Q(x):
	return mpmath.erfc(x/m.sqrt(2))/2
def F(x):
	return 1 - Q(x)
x = np.linspace(-5,5,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
vect_cdf = scipy.vectorize(F)
plt.plot(x.T,err,"x")
plt.plot(x.T,vect_cdf(x))
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

#if using termux
# plt.savefig('../figs/uni_cdf.pdf')
# plt.savefig('../figs/uni_cdf.eps')
# subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
# plt.savefig('../gau_cdf.pdf')
# plt.savefig('../gau_cdf.eps')
#subprocess.run(shlex.split("termux-open ../gau_cdf.pdf"))
#else
plt.show() #opening the plot window
