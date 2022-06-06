from SIR_Network_Simulation import Simulation
import matplotlib.pyplot as plt
from numpy import log as ln
import numpy as np
import networkx as nx


N = 100 # ln(N) = 6.2
k = 15
p = 0.5

# Use Watts Strogatz model to generate small world graph
G_WS = nx.watts_strogatz_graph(N, k, p)


def plot_graph(G):
    plt.figure(1)
    nx.draw(G, node_size=6)
    plt.show()


def verify_small_world(G):
    d_mean = nx.average_shortest_path_length(G)
    print("<d>:", d_mean)
    N = G.number_of_nodes()
    k_mean = 2 * G.number_of_edges() / N
    print("ln(N)/ln<k>:", ln(N) / ln(k_mean))


def avg_clustering(N, k):
    p = np.linspace(0, 0.01, num=501)
    ret = []
    for i in p:
        G = nx.watts_strogatz_graph(N, k, i, seed=1)
        avg_c = nx.average_clustering(G)
        ret.append(avg_c)
    return ret


def global_clustering(N, k):
    p = np.linspace(0, 0.01, num=501)
    ret = []
    for i in p:
        G = nx.watts_strogatz_graph(N, k, i, seed=1)
        global_c = nx.clustering(G)
        s = 0
        for k in global_c:
            s += global_c[k]
        ret.append(s / N)
    return ret


def avg_distance(N, k):
    p = np.linspace(0, 0.01, num=501)
    ret = []
    for i in p:
        G = nx.watts_strogatz_graph(N, k, i, seed=1)
        avg_d = nx.average_shortest_path_length(G)
        ret.append(avg_d)
    return ret


def diameter(N, k):
    p = np.linspace(0, 0.01, num=501)
    ret = []
    for i in p:
        G = nx.watts_strogatz_graph(N, k, i, seed=1)
        d = nx.diameter(G)
        ret.append(d)
    return ret


avg_clustering = avg_clustering(N, k)
# global_clustering = global_clustering(N, k)
avg_distance = avg_distance(N, k)
# diameter = diameter(N, k)
p = np.linspace(0, 0.01, num=501)

plt.plot(p, avg_clustering, label='avg clustering')
# plt.plot(p, global_clustering, label='global clustering')
plt.plot(p, avg_distance, label='avg distance')
# plt.plot(p, diameter, label='diameter')
plt.xlabel('p')
plt.legend()
plt.show()


# S = Simulation(G_WS, 0.2, 0.1)
# S.infect_list([i for i in range(3)])
# S.continuous_display()
