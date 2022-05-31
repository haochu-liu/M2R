from SIR_Network_Simulation import Simulation
import matplotlib.pyplot as plt
from numpy import log as ln
import networkx as nx


N = 100
k = 4
p = 0.5

# Use Watts Strogatz model to generate small world graph (?)
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


S = Simulation(G_WS, 0.2, 0.1)
S.infect_list([i for i in range(3)])
S.continuous_display()
