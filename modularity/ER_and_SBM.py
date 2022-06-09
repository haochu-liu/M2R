import networkx as nx
import EoN
import random
import numpy as np
import scipy.stats as stats
from math import sqrt
import matplotlib.pyplot as plt

N = 500
n = N / 2
sizes = [int(n), int(n)]
p_SBM = 0.1
k_SBM = [0.1, 0.01, 0.001]
prob_SBM = [[[p_SBM, k*p_SBM], [k*p_SBM, p_SBM]] for k in k_SBM]
prob_ER = p_SBM


def sir(G, r):
    initial_size = random.randint(0, N)
    tau = 1.
    gamma = r * tau
    t, S, I, R = EoN.fast_SIR(G, tau, gamma,
                              initial_infecteds=initial_size,
                              tmax=100)
    return t, S


def find_t(t, S):
    i = 0
    while S[i]/N >= 0.75:
        i += 1
        if i >= len(S):
            return None
    return t[i]


d_SBM = [[] for i in range(len(k_SBM))]
d_ER = []
r = 0.1

for n in range(100):
    G = nx.gnp_random_graph(N, prob_ER)
    t, S = sir(G, r)
    if find_t(t, S):
        d_ER.append(find_t(t, S))

for i in range(len(k_SBM)):
    for n in range(100):
        G = nx.stochastic_block_model(sizes, prob_SBM[i])
        t, S = sir(G, r)
        if find_t(t, S):
            d_SBM[i].append(find_t(t, S))


plt.hist(d_ER, bins=10, color='c', edgecolor='k', alpha=0.5, density=True)
plt.axvline(x=np.mean(d_SBM[0]))
plt.axvline(x=np.mean(d_SBM[1]))
plt.axvline(x=np.mean(d_SBM[2]))

mu = np.mean(d_ER)
var = np.var(d_ER)
x = np.linspace(0, np.mean(d_SBM[2]), 500)
y = stats.norm.pdf(x, loc=mu, scale=sqrt(var))
plt.plot(x, y)
plt.show()
print(stats.norm.cdf(np.mean(d_SBM[0]), loc=mu, scale=sqrt(var)))
print(stats.norm.cdf(np.mean(d_SBM[1]), loc=mu, scale=sqrt(var)))
print(stats.norm.cdf(np.mean(d_SBM[2]), loc=mu, scale=sqrt(var)))
