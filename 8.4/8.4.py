from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt
import math as m
import mpmath
import scipy


def Q(x):
	return mpmath.erfc(-x/m.sqrt(2))/2

r1= np.loadtxt('gau1.dat',dtype='double')
r2 = np.loadtxt('gau2.dat',dtype='double')
x = np.arange(0,10,step = 0.1)#points on the x axis
def stimulation(a):
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

vect_Q= scipy.vectorize(Q)
Vect = scipy.vectorize(stimulation, otypes=['double'])

plt.plot(x, Vect(x),'x')
plt.plot(x,vect_Q(x))
plt.xlabel('$A(dB)$')
plt.ylabel('$P_e(A)$')
plt.legend(["stimulation","Theory"])
plt.grid() #creating the grid
#plt.xlabel('$A$ (dB)')
#plt.ylabel('$P_e(A)$')
# plt.legend(["stimulation"])
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





