import networkx as nx
import matplotlib.pyplot as plt

test_arc_list=[(1, 2), (2, 3), (3, 4), (3, 5), (2, 5)]
multi_g=nx.MultiGraph()

multi_g.add_edges_from(test_arc_list)
print(nx.connected_components(multi_g))
print(nx.degree_centrality(multi_g))
print(nx.closeness_centrality(multi_g))
print(nx.betweenness_centrality(multi_g))


nx.draw(multi_g)
plt.savefig("draw.png")
plt.close()

nx.draw_random(multi_g)
plt.savefig("draw_random.png")
plt.close()
#nx.draw_random(multi_g)
#nx.draw_circular(multi_g)
#nx.draw_spectral(multi_g)

#plt.show()
