import networkx as nx
import matplotlib.pyplot as plt
import random as rnd

print(nx.__version__)
#arc_lst=[(i, j, rnd.random() )for i in range(1, 10) for j in range(1, 10) ]
#arc_lst=[ [ i, j, rnd.randint(7, 10) ] for i in range(1, 10) for j in range(1, 10) ]
g=nx.Graph()
#g.add_weighted_edges_from([ (1, 2, 10), (2, 3, 0.9) ])
g.add_weighted_edges_from([(i, j, rnd.random() ) for i in range(0, 5) for j in range(0, 5)])

print(g.edges(data=True))
#g2.add_weighted_edges_from((1, 2, 0.5), (2, 3, 0.9))
print("centrality")
print(nx.degree_centrality(g))
print("closeness")
print(nx.closeness_centrality(g))
print(nx.closeness_centrality(g, distance="weight"))
print("betweenness")
print(nx.betweenness_centrality(g))
print(nx.betweenness_centrality(g, weight="weight"))

print("clustering")
#print(nx.clustering(g, 0))
##drawing graph
nx.draw(g)
plt.savefig("draw.png")
plt.close()

nx.draw_random(g)
#plt.set_title("g, draw_random")
plt.savefig("draw_random.pdf")
plt.close()
#nx.draw_random(multi_g)
#nx.draw_circular(multi_g)
#nx.draw_spectral(multi_g)

#plt.show()
