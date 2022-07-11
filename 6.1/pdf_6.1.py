# Importing numpy, mpmath, scipy and matplotlib.pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

import math

maxrange=50
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1)
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('Chi.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

def pdf_Chi(x):
    if (x<0):
       return 1e-5
    elif (x>=0):
       return (math.exp((-x)/2)*0.5)
	
Vect_pdf_Chi = scipy.vectorize(pdf_Chi)

plt.plot(x[0:(maxrange-1)].T,pdf,'x')
plt.plot(x,Vect_pdf_Chi(x))#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])


plt.show() #opening the plot window
