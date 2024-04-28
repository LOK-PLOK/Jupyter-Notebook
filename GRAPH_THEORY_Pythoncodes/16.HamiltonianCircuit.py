

import networkx as nx
import matplotlib.pyplot as plt
# Create an empty undirected graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12])

# Add edges to the graph
edgelist = [(1, 2), (2, 3), (3, 4), (1, 5),(5, 6),(2,6),(6, 7),(3,7),(7, 8),(4,8),(5, 9),(9,10),(6,10),(10,11),(7,11),(11,12),(8,12)]
G.add_edges_from(edgelist)

# Draw the graph
nx.draw(G, with_labels=True)

# Display the plot
plt.show()