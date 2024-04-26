import matplotlib.pyplot as plt
import networkx as nx
seed = 200
# Use seed for reproducibility
G = nx.Graph()

# Add nodes
G.add_nodes_from([1,2,3,4,5,6,7])
# Add self-loops to the remaining nodes
edgelist = [(1,1),(1,2),(2,3),(2,4),(2,5),(3,6),(5,4)]
G.add_edges_from(edgelist)
#pos = nx.spring_layout(G, seed=seed)  # Seed for reproducible layout
pos = nx.planar_layout(G)
nx.draw(G, pos=pos,with_labels=True)
plt.show()