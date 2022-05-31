import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


class Simulation:
    def __init__(self, graph, beta, gamma) -> None:
        self.SUS = 1
        self.INF = 2
        self.REC = 3
        self.beta = beta
        self.gamma = gamma
        self.nodeStatuses = [self.SUS for _ in range(graph.number_of_nodes())]
        self.G = graph

    def infect(self, index):
        self.nodeStatuses[index] = self.INF

    def infect_list(self, indices):
        for i in indices:
            self.infect(i)

    def timestep(self):
        for node in self.G:
            if self.nodeStatuses[node] == self.INF:
                for neighbour in self.G.neighbors(node):
                    if (random.random() < self.beta and 
                            self.nodeStatuses[neighbour] == self.SUS):
                        self.nodeStatuses[neighbour] = self.INF
                if random.random() < self.gamma:
                    self.nodeStatuses[node] = self.REC

    def get_col(self, status):
        if status == self.SUS:
            return "blue"
        if status == self.INF:
            return "red"
        return "green"

    def get_col_map(self):
        return [self.get_col(status) for status in self.nodeStatuses]

    def display_network(self):
        random_pos = nx.random_layout(self.G, seed=42)
        pos = nx.spring_layout(self.G, pos=random_pos)
        nx.draw(self.G, node_color=self.get_col_map(), pos=pos, with_labels=True)
        plt.show()

    def animate(self, _):
        random_pos = nx.random_layout(self.G, seed=42)
        pos = nx.spring_layout(self.G, pos=random_pos)
        nx.draw(self.G, node_color=self.get_col_map(), pos=pos, with_labels=True)
        # plt.show()
        self.timestep()

    def continuous_display(self):
        anim = animation.FuncAnimation(plt.gcf(), self.animate, frames=20, interval=20)
        plt.show()


# Example
# N = 100
# G = nx.gnp_random_graph(N, 0.05, seed=42)
# S = Simulation(G, 0.2, 0.1)
# S.infect_list([i for i in range(3)])
# S.continuous_display()
