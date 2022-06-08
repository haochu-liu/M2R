import networkx as nx
import EoN
import matplotlib.pyplot as plt

G = nx.configuration_model([1,5,10]*100)
initial_size = 5
gamma = 1.
tau = 0.3
t, S, I, R = EoN.fast_SIR(G, tau, gamma,
                            initial_infecteds = range(initial_size))

plt.plot(t, I)
plt.plot(t, S)
plt.plot(t, R)
plt.show()
