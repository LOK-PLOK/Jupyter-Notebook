import networkx as nx
import matplotlib.pyplot as plt
seed = 40
# Create an empty undirected graph
G = nx.Graph()

# Add nodes to the graph
# G.add_nodes_from([1, 2, 3, 4, 5])
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])



edgelist = [(1, 2), (2, 3), (3, 4), (4, 5), (6, 1), (6, 5), (7, 5), (7, 4), (8, 4), (8, 3),(4,6), (2, 4)]
# Add edges to the graph
G.add_edges_from(edgelist)

# Draw the graph
nx.draw(G, with_labels=True)

# Display the plot
plt.show()