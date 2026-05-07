import numpy as np

def q(x):
    return x**2

def dqdx(x):
    return 2*x

def d2qdx2(x):
    return 2

def c(x):
    return x**3 + x**2

def dcdx(x):
    return 3*(x**2)+2*x

def d2cdx2(x):
    return 6*x + 2

def newton(dfdx, d2fdx2, x0, tol):

    x = []
    x.append(x0)
    n = 0
    # Used to debug
    #print(x)

    while dfdx(x[n])/dfdx(x0) > tol:
      
        x.append(x[n] - ((dfdx(x[n])) / d2fdx2(x[n])))
        n += 1
        # Used to debug
        #print(x)

        if n >= 1000:
            print("Breaking out of loop")
            break


    return x[n]

#print(newton(dqdx, d2qdx2, 20, 1e-05))
#print(newton(dcdx, d2cdx2, 1, 1e-08))


# ---- Q7 ii) ---- #


def rosenbrock(x, a=2, b=100):
    return (a-x[0])^2 + b*(x[1]-(x[0])**2)**2

def ddrddx0(x, a=2, b=100):
    return 2 + 8*b*(x[0])**2 - 4*b*(x[1] - (x[0])**2)

def ddrddx1(x, a=2, b=100):
    return 2*b

def ddrdx1dx0(x, a=2, b=100):
    return -4*b*x[0]

def J(x, a=2, b=100):

    return np.array([[ddrddx0(x, a, b), ddrdx1dx0(x, a, b)],
                     [ddrdx1dx0(x, a, b), ddrddx1(x, a, b)]])

print(newton(rosenbrock, J, [1.1, 1.1], 10e-09))


