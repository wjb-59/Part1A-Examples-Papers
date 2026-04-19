import numpy as np
import matplotlib.pyplot as plt

# Define parameters
t_min = 0
t_max = 20
n = 2000
k = 40
m = 1
dt = (t_max - t_min)/n


times = np.arange(0, 20, dt)

X = np.zeros(n)
X[0], X[1] = 0.01, 0.01


def f(x, F):

    #tester = 0
    for i in range(2, len(times)):
        
        x[i] = (dt*dt)*F/m + 2*x[i-1] - (k/m)*dt*dt*x[i-1] - x[i-2]
        
        #tester += 1
        #if tester % 5 == 0:
        #   print(x[i])
    return(x)

Analytical = 0.01*np.cos(np.sqrt(k/m)*times)

# Tests to check dimensions of the lists (was getting an error before)
#print(len(X))
#print(len(times))
#print(len(Analytical))

# Part b)
plt.plot(times, f(X, 0), label='Numeric Solution')
plt.plot(times, Analytical, label='Exact Solution')

plt.xlabel("t")
plt.ylabel("x")
plt.legend(loc=1)

plt.figure()
plt.close(2)

plt.show()

# Part c)
plt.plot(times, f(X, 0.25), label='Numeric Solution')
plt.plot(times, Analytical, label='Exact Solution')

plt.xlabel("t")
plt.ylabel("x")
plt.legend(loc=1)

plt.figure()
plt.close(2)

plt.show()