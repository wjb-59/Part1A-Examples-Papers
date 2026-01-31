import numpy as np
import matplotlib

# Define parameters
dt = 0.01
n = 20000

times = np.array(0, 20, dt)

def f(x):
    
    return x()