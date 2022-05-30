import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def sirs_func(y, t, beta, gamma, delta):
    s, x, r = y
    ret = [delta*r - beta*s*x, beta*s*x - gamma*x, gamma*x - delta*r]
    return ret


def plot_sirs(beta, gamma, delta, x0, t):
    y0 = [1 - x0, x0, 0]
    sol = odeint(sirs_func, y0, t, args=(beta, gamma, delta))

    plt.plot(t, sol[:, 0], 'b', label='s(t)')
    plt.plot(t, sol[:, 1], 'r', label='x(t)')
    plt.plot(t, sol[:, 2], 'g', label='r(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.show()


# t = np.linspace(0, 50, 501)
# plot_sirs(beta=1, gamma=0.5, delta=0.2, x0=0.01, t=t)
