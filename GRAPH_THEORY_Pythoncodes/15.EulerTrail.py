import networkx as nx
import matplotlib.pyplot as plt
# Create an empty undirected graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from([1, 2, 3, 4, 5, 6])

# Add edges to the graph
edgelist = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,1),(6,2),(6,4),(2,4)]
G.add_edges_from(edgelist)

# Draw the graph
nx.draw(G, with_labels=True)

# Display the plot
plt.show()