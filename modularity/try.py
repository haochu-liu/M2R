import networkx as nx
import EoN
import random
import numpy as np
import matplotlib.pyplot as plt

p_er = 0.01
N = 500
G = nx.gnp_random_graph(N, p_er)
tau = 0.1
gamma = 0.05
full_data = EoN.fast_SIR(G, tau, gamma,
                         tmax=10,
                         return_full_data=True)
full_data.display(2)
plt.show()
