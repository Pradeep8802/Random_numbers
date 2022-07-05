import numpy as np

#Contains values of the gaussian distribution
nor = np.loadtxt('gau.dat', dtype='float')

#Contains values of the bernolli distribution
ber = np.loadtxt('ber5.dat', dtype='float')

# Y = A*X + N
Y = 5*ber + nor

e0 = np.count_nonzero((Y < 0) & (ber > 0))
n0 = np.count_nonzero(ber > 0)
e1 = np.count_nonzero((Y > 0) & (ber < 0))
n1 = np.count_nonzero(ber < 0)
print("For X=1, percentage of wrong labels : ", float(e0/n0))
print("For X=-1, percentage of wrong labels : ", float(e0/n0))
