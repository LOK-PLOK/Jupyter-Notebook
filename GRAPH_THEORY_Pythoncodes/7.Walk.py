import networkx as nx
import matplotlib.pyplot as plt
seed = 40
# Create an empty undirected graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges to the graph
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 1)])

# Draw the graph
nx.draw(G, with_labels=True)

# Display the plot
plt.show()