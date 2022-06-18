import networkx as nx
import EoN
import matplotlib.pyplot as plt

G = nx.watts_strogatz_graph(100, 10, 0.01)
gamma = 1.
tau = 0.3
full_data = EoN.fast_SIR(G, tau, gamma,
                            initial_infecteds = range(initial_size),
                            return_full_data=True)
full_data.display()
