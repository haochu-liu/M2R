import networkx as nx
import EoN
import matplotlib.pyplot as plt

G = nx.configuration_model([1,5,10]*100)
initial_size = 2
gamma = 1.
tau = 0.3
full_data = EoN.fast_SIR(G, tau, gamma,
                          initial_infecteds=range(initial_size),
                          return_full_data=True)

print(full_data.node_history(10))
