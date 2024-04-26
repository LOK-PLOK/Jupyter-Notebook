import networkx as nx
import matplotlib.pyplot as plt
seed = 21
# Create a directed graph object
G = nx.DiGraph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5, 6,7])

# Add edges to the graph
G.add_edge(1, 5)
G.add_edge(5, 2)
G.add_edge(2, 6)
G.add_edge(6, 3)
G.add_edge(3, 7)
G.add_edge(7, 4)
G.add_edge(4, 1)


# Draw the graph
pos = nx.circular_layout(G)
nx.draw(G,pos=pos, with_labels=True)

# Show the plot
plt.show()