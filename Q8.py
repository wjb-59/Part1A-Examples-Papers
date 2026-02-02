import random
import numpy as np

def monte_carlo(f, N, x_b, x_a, y_b, y_a):

    total = 0
    num_it = 0

    while num_it < N:
        total += f(random.randint(x_a, x_b), random.randint(y_a, y_b))
        num_it += 1

    f_bar = total/N
    return(f_bar)

def part_a(x, y):

    value = np.exp(x*y)*(np.cos(y)**2)*(np.sin(x*x))

    return value


# This code doesn't work with the monte carlo method - so doesn't work here
def part_b(x, y=1):

    value = np.sqrt(1-(x**2))*y

    return value

# Part a)
print("Monte Carlo with N = 10^2:", monte_carlo(part_a, 10**2, 1, -1, 1, -1))
print()
print("Monte Carlo with N = 10^5:", monte_carlo(part_a, 10**5, 1, -1, 1, -1))
print()
print("Monte Carlo with N = 10^6:", monte_carlo(part_a, 10**6, 1, -1, 1, -1))
print()

# Part b)
#print("Monte Carlo with N = 10^2:", monte_carlo(part_b, 10**2, 1, -1, 1, -1))
#print()
#print("Monte Carlo with N = 10^5:", monte_carlo(part_b, 10**5, 1, -1, 1, -1))
#print()
#print("Monte Carlo with N = 10^6:", monte_carlo(part_b, 10**6, 1, -1, 1, -1))
#print()