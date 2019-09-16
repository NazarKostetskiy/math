import numpy as np
from scipy.interpolate import interp1d
import pylab

A, nu, k = 10, 4, 2

# def f(x, A, nu, k):
#     return A * np.exp(-k*x) * np.cos(2*np.pi * nu * x)

def f(x):
    return 1 / (6 * (x ** 3) - 5 * x - 5)

xmax, nx = 0.5, 8
x = np.linspace(0, xmax, nx)
y = f(x)

f_nearest = interp1d(x, y, kind='nearest')
f_linear  = interp1d(x, y)
print(f_linear)
print(f_nearest)

