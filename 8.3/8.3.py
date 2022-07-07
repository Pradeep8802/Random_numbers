from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import math as m
import mpmath
import scipy
r1= np.loadtxt('gau.dat',dtype='double')
r2 = np.loadtxt('gau.dat',dtype='double')
x = np.arange(0,10,step = 0.1)#points on the x axis
def numerical(a):
    c1=0
    c2=0
    c3=0
    c4=0
    for i in range(1000000):
        if(-a<r1[i] and r2[i]<0):
            c1+=1
        elif(-a<r1[i] and r2[i]>0):
            c2+=1
        elif(-a>r1[i] and r2[i]<0):
            c3+=1
        elif(-a>r1[i] and r2[i]>0):
            c4+=1
    return 2*c1/(c1+c2+c3+c4)

    # n0 = np.count_nonzero(ber > 0)
    # n1 = np.count_nonzero(ber < 0)
    # e0 = np.count_nonzero((Y < 0) & (ber > 0)) 
    # e1 = np.count_nonzero((Y > 0) & (ber < 0))
    # p0=e0/n0
    # p1=e1/n1
    # return (p0+p1)*0.5

Vect = scipy.vectorize(numerical, otypes=['double'])
plt.plot(x, Vect(x))
plt.grid() #creating the grid
#plt.xlabel('$A$ (dB)')
#plt.ylabel('$P_e(A)$')
# plt.legend(["Numerical"])
#if using termux
# plt.savefig('../figs/uni_cdf.pdf')
# plt.savefig('../figs/uni_cdf.eps')
# subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
# plt.savefig('../gau_cdf.pdf')
# plt.savefig('../gau_c,"Theoriticaldf.eps')
#subprocess.run(shlex.split("termux-open ../gau_cdf.pdf"))
#else
plt.show() 





