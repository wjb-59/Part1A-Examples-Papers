import numpy as np

def f(x):
    return x**3 + 3*x**2 + 8*x + 6

def anl_der(x):
    return 3*x**2 + 6*x + 8

def one_sided_der(x, h):
    return (f(x+h)-f(x))/h

def sym_dif_der(x, h):
    return (f(x+h)-f(x-h))/(2*h)

step = [1e-02, 1e-04, 1e-06]
x = 5

for h in step:
    print(h)
    print()
    print("Analytical: {}".format(anl_der(x)))
    print()
    print("One Sided Numeric: {}".format(one_sided_der(x, h)))
    print("Error: {}".format(one_sided_der(x, h) - anl_der(x)))
    print()
    print("Symmetric Numeric: {}".format(sym_dif_der(x, h)))
    print("Error: {}".format(sym_dif_der(x, h) - anl_der(x)))
    print("*****")