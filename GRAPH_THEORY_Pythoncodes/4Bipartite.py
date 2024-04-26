import matplotlib.pyplot as plt
import networkx as nx

Chika = nx.Graph()
Chika.add_nodes_from(['Paul','Luis','Elijah'], bipartite=0) # Add the node attribute "bipartite"
Chika.add_nodes_from(['Sharley','Hasm','Edouard'], bipartite=1)
Chika.add_edges_from([('Paul','Sharley'), ('Paul','Hasm'),('Paul','Edouard')
                    , ('Luis','Sharley'), ('Luis','Hasm'),('Luis','Edouard')
                    , ('Elijah','Sharley'), ('Elijah','Hasm'),('Elijah','Edouard')])

top = nx.bipartite.sets(Chika)[0]
pos = nx.bipartite_layout(Chika, top)
nx.draw(Chika, pos=pos, with_labels=True, node_color=['pink','magenta','red','deepskyblue','cyan','green'])
plt.show()
