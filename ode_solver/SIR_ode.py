import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def sir_func(y, t, beta, gamma):
    s, x, r = y
    ret = [-beta*s*x, beta*s*x - gamma*x, gamma*x]
    return ret


def plot_sir(beta, gamma, x0, t):
    y0 = [1 - x0, x0, 0]
    sol = odeint(sir_func, y0, t, args=(beta, gamma))

    plt.plot(t, sol[:, 0], 'b', label='s(t)')
    plt.plot(t, sol[:, 1], 'r', label='x(t)')
    plt.plot(t, sol[:, 2], 'g', label='r(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.show()


# t = np.linspace(0, 50, 501)
# plot_sir(beta=1, gamma=0.5, x0=0.01, t=t)
