from SIR_Network_Simulation import Simulation
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx


N = 1000
L = 4

G_BA = nx.barabasi_albert_graph(N, L)


def plot_graph(G):
    plt.figure(1)
    nx.draw(G, node_size=6)
    plt.show()


def plot_degree(G):
    h_BA = nx.degree_histogram(G)
    N = G.number_of_nodes()
    plt.plot(np.array(h_BA) / N, 'x')
    plt.xlabel('degree')
    plt.ylabel('fraction of nodes')
    plt.title('Degree distributions of Barabasi-Albert graphs')
    plt.grid()
    plt.show()


def plot_degree_log(G):
    h_BA = nx.degree_histogram(G)
    N = G.number_of_nodes()
    plt.loglog(np.array(h_BA) / N, 'x')
    plt.xlabel('degree')
    plt.ylabel('fraction of nodes')
    plt.title('Degree log distributions of Barabasi-Albert graphs')
    plt.grid()
    plt.show()


S = Simulation(G_BA, 0.2, 0.1)
S.infect_list([i for i in range(3)])
S.continuous_display()
