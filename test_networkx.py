import networkx as nx
import matplotlib.pyplot as plt
import random as rnd

print("networkx version: "+nx.__version__)
#arc_lst=[(i, j, rnd.random() )for i in range(1, 10) for j in range(1, 10) ]
#arc_lst=[ [ i, j, rnd.randint(7, 10) ] for i in range(1, 10) for j in range(1, 10) ]
g=nx.Graph()
uw_g=nx.Graph()
m_g=nx.MultiGraph()
g.add_weighted_edges_from([ ("a", "b", 8), ("b", "c", 10), ("c", "d", 133), ("d", "e", 3) ])
uw_g.add_edges_from([ ("a", "b"), ("b", "c"), ("c", "d"), ("d", "e") ])
for elem in g.edges(data=True):
	print(elem)
	for i in range(0, elem[2]["weight"]):
		m_g.add_edge(elem[0], elem[1]) 
#g.add_weighted_edges_from([( i, j, rnd.random() ) for i in range(0, 5) for j in range(0, 5)])

print(g.edges(data=True))
#g2.add_weighted_edges_from((1, 2, 0.5), (2, 3, 0.9))
print(nx.info(g))
print(nx.info(m_g))
print("Degree")
print(nx.degree(g))
print(nx.degree(uw_g))
print(nx.degree(m_g))
print("centrality")
print(nx.degree_centrality(g))
print(nx.degree_centrality(uw_g))
print(nx.degree_centrality(m_g))
print("closeness")
print(nx.closeness_centrality(g))
print(nx.closeness_centrality(uw_g))
print(nx.closeness_centrality(g, distance="weight"))
print(nx.closeness_centrality(m_g))
print("betweenness")
print(nx.betweenness_centrality(g))
print(nx.betweenness_centrality(uw_g))
print(nx.betweenness_centrality(g, weight="weight"))
print(nx.betweenness_centrality(m_g))

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

nx.draw_circular(g)
plt.savefig("draw_circular.pdf")
plt.close()

nx.draw_spectral(g)
plt.savefig("draw_spectral.pdf")
plt.close()
#nx.draw_random(multi_g)
#nx.draw_circular(multi_g)
#nx.draw_spectral(multi_g)

#plt.show()
