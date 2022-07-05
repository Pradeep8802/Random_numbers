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

A = np.linspace(0, 10, 30)
#Contains values of the normal distribution
nor = np.loadtxt('gau.dat', dtype='float')

#Contains values of the bernolli distribution
ber = np.loadtxt('ber5.dat', dtype='float')

# Y = A*X + N
#Y = a*ber + nor
def numerical(a):
    Y = a*ber + nor
    n0 = np.count_nonzero(ber > 0)
    n1 = np.count_nonzero(ber < 0)
    e0 = np.count_nonzero((Y < 0) & (ber > 0)) 
    e1 = np.count_nonzero((Y > 0) & (ber < 0))
    p0=e0/n0
    p1=e1/n1
    return (p0+p1)*0.5

Vect_num = scipy.vectorize(numerical, otypes=['float'])

Q_func = scipy.vectorize(Q)

plt.plot(A, Vect_num(A),'x')
plt.plot(A.T,Q_func(A))

plt.grid() #creating the grid
plt.xlabel('$A$ (dB)')
plt.ylabel('$P_e(A)$')
plt.legend(["Numerical","Theoritical"])
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
