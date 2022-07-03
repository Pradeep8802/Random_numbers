#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt

# #if using termux
# import subprocess
# import shlex
#end if

x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

#Uniform random variable cdf for a=0 and b=1 in the definition of uniform random variable
def cdfUniform(x):
	if(x<=0):
		x=0
	elif(x>1):
		x=1
	return x
    
theoritical = []
for i in range(len(x)):
	theoritical.append(cdfUniform(x[i]))


plt.plot(x,err,'x')
plt.plot(x,theoritical)#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$F_X(x_i)$')
plt.legend(["Numerical","Theory"])

# #if using termux
# plt.savefig('../figs/uni_cdf.pdf')
# plt.savefig('../figs/uni_cdf.eps')
# subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window
