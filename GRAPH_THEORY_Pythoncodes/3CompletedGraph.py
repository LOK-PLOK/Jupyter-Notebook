import networkx as nx
import matplotlib.pyplot as plt

# Create a complete graph with 6 nodes
G = nx.complete_graph(5)

# Draw the graph
nx.draw(G, with_labels=True)

# Display the plot
plt.show()