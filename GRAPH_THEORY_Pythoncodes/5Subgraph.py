import networkx as nx
import matplotlib.pyplot as plt
seed = 49
# Create a complete graph with 6 nodes
G = nx.complete_graph(4)

# Draw the graph
nx.draw(G, with_labels=True)

# Display the plot
plt.show()
import networkx as nx
import matplotlib.pyplot as plt
seed = 49
# Create a complete graph with 6 nodes
G = nx.complete_graph(3)

# Draw the graph
nx.draw(G, with_labels=True)

# Display the plot
plt.show()