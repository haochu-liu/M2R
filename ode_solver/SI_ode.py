import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def si_func(y, t, beta):
    s, x = y
    ret = [-beta * s * x, beta * s * x]
    return ret


def plot_si(beta, x0, t):
    y0 = [1 - x0, x0]
    sol = odeint(si_func, y0, t, args=(beta,))

    plt.plot(t, sol[:, 0], 'b', label='s(t)')
    plt.plot(t, sol[:, 1], 'r', label='x(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.show()


# t = np.linspace(0, 10, 101)
# plot_si(beta=1, x0=0.01, t=t)
