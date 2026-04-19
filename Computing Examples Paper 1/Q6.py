import numpy as np

# Define function
def f(x):
    return (x**3 + x**2)

# Compute numerical integration
def num_int(f , x, a, b, w):
    
    value = 0
    # Iterate over all values for x and w
    for i in range(len(x)):

        value += w[i] * f(x[i])

    total = (b-a)*value

    return total

# Define limits
a = 0
b = 10

# Define exact solution
exact = 8500/3

# Define x
x_a = (a, b)
x_b = (a, (a+b)/2, b)
x_c = ((a+b)/2-((b-a)/(2*np.sqrt(3))), (a+b)/2+((b-a)/(2*np.sqrt(3))))

# Define w
w_a = (0.5, 0.5)
w_b = (1/6, 2/3, 1/6)
w_c = (0.5, 0.5)

# Question a output
print("Trapezoidal Rule:{}".format(num_int(f, x_a, a, b, w_a)))
print("Error is: {}".format(abs(num_int(f, x_a, a, b, w_a)-(exact))))
print()

# Question b output
print("Simpson's Rule:{}".format(num_int(f, x_b, a, b, w_b)))
print("Error is: {}".format(abs(num_int(f, x_b, a, b, w_b)-(exact))))
print()

# Question c output
print("Gauss Quadrature:{}".format(num_int(f, x_c, a, b, w_c)))
print("Error is: {}".format(abs(num_int(f, x_c, a, b, w_c)-(exact))))
print()