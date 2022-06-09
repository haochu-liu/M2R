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
    tau = 0.1
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

mu = np.mean(d_ER)
var = np.var(d_ER)
theta = var / mu
k = mu / theta
x = np.linspace(0, 3, 300)
y = stats.gamma.pdf(x, k, scale=theta)
plt.plot(x, y, color='c')
p1 = stats.gamma.cdf(np.mean(d_SBM[0]), k, scale=theta)
p2 = stats.gamma.cdf(np.mean(d_SBM[1]), k, scale=theta)
p3 = stats.gamma.cdf(np.mean(d_SBM[2]), k, scale=theta)

plt.hist(d_ER, bins=20, color='b', edgecolor='none', alpha=0.6, density=True)
plt.axvline(x=np.mean(d_SBM[0]), color='k', linestyle='-.', label='mean $t_{SBM}}$ of k = 0.1')
plt.axvline(x=np.mean(d_SBM[1]), color='k', linestyle='--', label='mean $t_{SBM}$ of k = 0.01')
plt.axvline(x=np.mean(d_SBM[2]), color='k', linestyle=':', label='mean $t_{SBM}$ of k = 0.001')
plt.xlabel('t')
plt.ylabel('Density')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=1, fancybox=True, shadow=False)
plt.show()
print(1-p1, 1-p2, 1-p3)
