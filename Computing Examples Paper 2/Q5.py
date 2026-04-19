import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return (np.sin(x)) + (np.cos(10*x))/5

def tpa(x):
    data = []

    data.append(x[0])
    for n in range(1, len(x)-1):
        data.append((x[n-1] + x[n] + x[n+1])/3)
    data.append(x[(len(x))-1])

    return data

# create data set
X = np.linspace(0, (2*np.pi), 50)
Y = f(X)
Avg = tpa(Y)

plt.plot(X, Y, X, Avg)
plt.show()