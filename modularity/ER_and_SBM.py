import networkx as nx
import EoN
import numpy as np
import matplotlib.pyplot as plt

N = 500
p_er = 0.01
l = N*(N-1)*p_er/2


def p_2_sbm(N, r):
    n = N / 2
    sizes = [int(n), int(n)]
    p = l / (n*n*r + n*(n-1))
    return sizes, [[p, r*p], [r*p, p]]


def p_3_sbm(N, r):
    n = N / 3
    sizes = [int(n), int(n), int(n)]
    p = l / (3*r*n*n + 3*n*(n-1)/2)
    return sizes, [[p, r*p, r*p], [r*p, p, r*p], [r*p, r*p, p]]


def p_4_sbm(N, r):
    n = N / 4
    sizes = [int(n), int(n), int(n), int(n)]
    p = l / (6*r*n*n + 2*n*(n-1))
    return sizes, [[p, r*p, r*p, r*p], [r*p, p, r*p, r*p], [r*p, r*p, p, r*p], [r*p, r*p, r*p, p]]


def sir_t(G, t):
    tau = 0.05
    gamma = 0.05
    full_data = EoN.fast_SIR(G, tau, gamma,
                             tmax=10,
                             return_full_data=True)
    s = 0
    for i in range(N):
        if full_data.node_status(i, t) != 'S':
            s += 1
    return s/N


list_r = np.logspace(-4, 0, base=10.0, num=51)
# n_er = []
n_sbm = []
r_sbm = []
n_m_sbm = []
r_m_sbm = []
n_v_sbm = []
t = 10.0

# for i in range(20):
#     G = nx.gnp_random_graph(N, p_er)
#     s = sir_t(G, t)
#     n_er.append(s)

for r in list_r:
    sizes, p = p_4_sbm(N, r)
    list_s = []
    for i in range(50):
        G = nx.stochastic_block_model(sizes, p)
        s = sir_t(G, t)
        list_s.append(s)
        n_sbm.append(s)
        r_sbm.append(np.log10(r))
    r_m_sbm.append(np.log10(r))
    n_m_sbm.append(np.mean(list_s))
    n_v_sbm.append(np.std(list_s))

plt.scatter(r_sbm, n_sbm, alpha=0.25)
plt.plot(r_m_sbm, n_m_sbm, 'b', linestyle=':')
plt.xlabel('ln(p2/p1)')
plt.ylabel('Infected or recovered nodes')
plt.show()

plt.plot(r_m_sbm, n_v_sbm)
plt.show()
