import networkx as nx
import EoN
import numpy as np
import random
import matplotlib.pyplot as plt

sizes = [50, 50]
probs = [[0.1, 0.001], [0.001, 0.1]]

G = nx.stochastic_block_model(sizes, probs)

initial_size = random.randint(0, 99)
gamma = 0.25
tau = 1
full_data = EoN.fast_SIR(G, tau, gamma,
                         initial_infecteds=initial_size,
                         return_full_data=True)

t = full_data.t()
I = full_data.I()
S = full_data.S()
R = full_data.R()

full_data.display(2, node_size=50)
plt.show()

C_1 = list(range(50))
C_2 = list(range(50, 100))
C_1_I = []
C_2_I = []

for i in t:
    i1, i2 = 0, 0
    for j in C_1:
        status = full_data.node_status(j, i)
        if status == 'I':
            i1 += 1
    for k in C_2:
        status = full_data.node_status(k, i)
        if status == 'I':
            i2 += 1
    C_1_I.append(i1)
    C_2_I.append(i2)

plt.plot(t, C_1_I, label='I(t) for cluster 1')
plt.plot(t, C_2_I, label='I(t) for cluster 2')
plt.xlabel('t')
plt.ylabel('Number of nodes')
plt.legend(loc='best')
plt.show()
