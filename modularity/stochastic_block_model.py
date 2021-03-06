from SIR_Network_Simulation import Simulation
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from scipy.linalg import eigh

sizes = [50, 50]
probs = [[0.1, 0.001], [0.001, 0.1]]

G_sb = nx.stochastic_block_model(sizes, probs)


def plot_graph(G):
    col = ['blue' for i in range(50)] + ['red' for i in range(50)]
    plt.figure(1)
    nx.draw(G, node_size=50, node_color=col)
    plt.show()


def spectral_modularity(G):
    B = nx.modularity_matrix(G)
    N = G.number_of_nodes()
    e1, v1 = eigh(B, eigvals=(N-1, N-1))
    e1 = e1[0]
    v1 = v1[:, 0]
    s = np.ones_like(v1)
    s[v1 < 0] = -1
    ind1p = np.where(s == 1)[0]
    ind1m = np.where(s == -1)[0]
    cSpectral = [set(ind1p), set(ind1m)]
    Mspectral = nx.algorithms.community.modularity(G, cSpectral)
    print("spectral modularity=", Mspectral)
    return cSpectral


def greedy_modularity(G):
    cGreedy = list(nx.algorithms.community.greedy_modularity_communities(G))
    Mgreedy = nx.algorithms.community.modularity(G, cGreedy)
    print("greedy modularity=", Mgreedy)
    return cGreedy


# plot_graph(G_sb)

# S = Simulation(G_sb, 0.05, 0.05)
# S.infect_list([i for i in range(2)])
# S.continuous_display()
