import numpy as np

def f(x):
    return (x**2)*(np.sin(x**2))

def analytical(x):
    return (2*x*(np.sin(x**2))+((x**2)*(2*x)*(np.cos(x**2))))

def comp_step(x, h):
    y = (f(x + (1j*h)))/h
    return y.imag

def sym_dif(x, h):
    return (f(x+h)-f(x-h))/(2*h)

X = [10, 100, 1000, 10000]
H = [1e-09, 1e-12, 1e-15]

for x in X:
    
    for h in H:
        print("x = {}".format(x))
        print("h = {}".format(h))
        print(sym_dif(x, h))
        print("Symmetric Difference Error is: {}".format(sym_dif(x, h) - analytical(x)))
        print(comp_step(x, h))
        print("Complex Step Error is: {}".format(comp_step(x, h) - analytical(x)))
        print()
    print("***")


#print(sym_dif((X[3]), H[2]))
#print(f(X[3]+H[1]))
#print(f(X[3]-H[1]))