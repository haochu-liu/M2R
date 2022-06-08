import networkx as nx
import EoN
import random
import numpy as np
import scipy.stats as stats 
import matplotlib.pyplot as plt

N = 500
n = N / 2
sizes = [int(n), int(n)]
p_SBM = 0.1
k_SBM = [0.02, 0.01, 0.005]
prob_SBM = [[[p_SBM, k*p_SBM], [k*p_SBM, p_SBM]] for k in k_SBM]
prob_ER = [(n*(n-1)*p_SBM + n*n*k*p_SBM) / (2*n*n) for k in k_SBM]


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
            return 100.0 # tmax
    return t[i]


d_SBM = []
d_ER = [[] for i in range(len(k_SBM))]
r = 0.2

for i in range(len(k_SBM)):
    for n in range(50):
        G = nx.gnp_random_graph(N, prob_ER[i])
        t, S = sir(G, r)
        d_ER[i].append(find_t(t, S))
    sum_t = 0
    for n in range(50):
        G = nx.stochastic_block_model(sizes, prob_SBM[i])
        t, S = sir(G, r)
        sum_t += find_t(t, S)
    d_SBM.append(sum_t / 50)


result = plt.hist(d_ER[2], bins=10, color='c', edgecolor='k', alpha=0.65)
plt.axvline(d_SBM[2], color='k', linestyle='dashed', linewidth=1)
# plt.show()

mu = np.mean(d_ER[2])
var = np.var(d_ER[2])
theta = var / mu
k = mu / theta
x = np.linspace(0, 1, 100)
y = stats.norm.pdf(x, loc=mu, scale=var)
plt.plot(x, y)
plt.show()
print(stats.gamma.cdf(d_SBM[2], a=k, scale=theta))
print(stats.norm.cdf(d_SBM[2], loc=mu, scale=var))
