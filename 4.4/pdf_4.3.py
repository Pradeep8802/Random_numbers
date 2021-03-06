#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt
import math

#if using termux
# import subprocess
# import shlex
#end if
maxrange=50
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
xx = np.linspace(-maxlim,maxlim,maxrange*50) #more points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1)
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('fourth1.dat',dtype='double')

for i in range(0,maxrange):
    err_ind = np.nonzero(randvar < x[i]) #checking probability condition
    err_n = np.size(err_ind) #computing the probability
    err.append(err_n/simlen) #storing the probability values in a list

    
for i in range(0,maxrange-1):
    test = (err[i+1]-err[i])/(x[i+1]-x[i])
    pdf.append(test) #storing the pdf values in a list


def pdf_traingular(x):
    y=x
    if(x<0):
        y=0
    elif(x>2):
        y=0
    elif(x>1 and x<2):
        y=2-x 
    return y           

    
vect_pdf = np.vectorize(pdf_traingular, otypes=[np.float])

plt.plot(x[0:(maxrange-1)].T,pdf, 'x')
plt.plot(xx,vect_pdf(xx))
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$Y$')
plt.legend(["Numerical","Theory"])

#if using termux
# plt.savefig('../figs/uni_pdf.pdf')
#plt.savefig('../figs/uni_pdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_pdf.pdf"))
#if using termux
# plt.savefig('../figs/gauss_pdf.pdf')
# plt.savefig('../figs/gauss_pdf.eps')
# subprocess.run(shlex.split("termux-open ../figs/gauss_pdf.pdf"))
#else
# plt.savefig('../figures/CDF_tri.png')
plt.show() #opening the plot window

# #Importing numpy, scipy, mpmath and pyplot
# import numpy as np
# import mpmath as mp
# import scipy 
# import matplotlib.pyplot as plt

# # #if using termux
# # import subprocess
# # import shlex
# # #end if


# maxrange=50
# maxlim=6.0
# x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
# simlen = int(1e6) #number of samples
# err = [] #declaring probability list

# h = 2*maxlim/(maxrange-1)
# #randvar = np.random.normal(0,1,simlen)
# #randvar = np.loadtxt('uni.dat',dtype='double')
# randvar = np.loadtxt('fourth1.dat',dtype='double')

# for i in range(0,maxrange):
#     err_ind = np.nonzero(randvar < x[i]) #checking probability condition
#     err_n = np.size(err_ind) #computing the probability
#     err.append(err_n/simlen) #storing the probability values in a list

# pdf = [] #Declaring pdf as a list
# for i in range(0,maxrange-1):
#     new_dat=(err[i+1]-err[i])/(x[i+1]-x[i])
#     pdf.append(new_dat) # Storing the pdf values in the list pdf created before 

# def pdf_traingular(x):
#     y=[]
#     for i in range(50):
#         if(x[i]>=0 and x[i]<1):
#             y.append(x)
#         elif(x[i]>=1 and x[i]<2):
#             y.append(2-x)
#         elif(x[i]<0 or x[i]>2):
#             y.append(0)                             
#     return y
# print(x)    
# vect_pdf= scipy.vectorize(pdf_traingular)

# plt.plot(x[0:(maxrange-1)].T,pdf,'x')
# plt.plot(x,vect_pdf(x))#plotting the CDF
# plt.grid() #creating the grid
# plt.xlabel('$x_i$')
# plt.ylabel('$p_X(x_i)$')
# plt.legend(["Numerical","Theory"])

# #if using termux
# #plt.savefig('../figs/uni_pdf.pdf')
# #plt.savefig('../figs/uni_pdf.eps')
# #subprocess.run(shlex.split("termux-open ../figs/uni_pdf.pdf"))
# #if using termux
# #plt.savefig('../figs/gauss_pdf.pdf')
# #plt.savefig('../figs/gauss_pdf.eps')
# #subprocess.run(shlex.split("termux-open ../figs/gauss_pdf.pdf"))
# #else
# plt.show() #opening the plot window


# # Two dices (rectangular) p = 1/6 use convolution
# #use built in



