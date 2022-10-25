import numpy as np
import matplotlib.pyplot as plt

a1 = np.array([4,6,8,2])
a2 = np.zeros(10)
a3 = np.ones(4)
a4 = np.random.random(10)
a5 = np.random.randn(10)
a6 = np.linspace(0, 10, 100)
a7 = np.arange(0, 10, 0.2)

a1 = 2*np.random.randn(10000) + 10
np.mean(a1)
np.std(a1)
np.percentile(a1, 80)
x = np.linspace(1, 10, 100)
y = 1/x**2 * np.sin(x)
dydx = np.gradient(y,x)
y_integral = np.cumsum(y) * (x[1]-x[0])
plt.plot(x,y)
plt.plot(x,dydx)
plt.plot(x,y_integral)

# Examples

#1 
N = 10000
x = np.linspace(0, 10, N+1)
y = np.exp(-x/10) * np.sin(x)
plt.plot(x,y)

#2
np.mean(y[(x>=4)*(x<=7)])
np.std(y[(x>=4)*(x<=7)])

#3 
np.percentile(y[(x>=4)*(x<=7)], 80)

#4
plt.plot(x, np.gradient(y,x))

#5
dydx = np.gradient(y,x)
x[1:][dydx[1:] * dydx[:-1] < 0]