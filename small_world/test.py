import networkx as nx

G = nx.watts_strogatz_graph(100, 10, 0.01)
sigma = nx.sigma(G, niter=10)
print(sigma)
