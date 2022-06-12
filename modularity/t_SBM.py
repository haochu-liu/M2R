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
k = 0.01
prob_SBM = [[p_SBM, k*p_SBM], [k*p_SBM, p_SBM]]


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


d_SBM = []
r = 0.1


for i in range(len(k_SBM)):
    for n in range(100):
        G = nx.stochastic_block_model(sizes, prob_SBM[i])
        t, S = sir(G, r)
        if find_t(t, S):
            d_SBM[i].append(find_t(t, S))


