
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

def dijkstra(graph, sources):
   
   tmp = graph.copy()
   push = heappush
   pop = heappop
   nodes = tmp.nodes()

   for x in nodes:
      tmp.node[x][l] = np.inf # l = lambda do algoritmo passado em sala
      tmp.node[x]['pi'] = None

   for x in souces:
      tmp.node[x][l] = 0

   fp = []
   s = []

   for x in nodes:
      push(fp, (tmp,node[x][l],x))

   while fp:

      u = pop(fp)
      u = u[1]
      s.append(u)

      for x in tmp.neighbors(u):
         if v not in s and tmp.node[v][l] > (tmp.node[u][l] + g[u][v]['s.weight']):
            q.remove(tmp.node[x][l],x)
            tmp.node[x][l] = tmp.node[u][l] + g[u][v]['s.weight']
            tmp.node[x]['pi']=u

   r = nx.Graph()

   for u in tmp.nodes():
      r.add_node(u)
      if tmp.node[u]['pi'] is not None:
         r.add_edge(u,tmp.node[u]['pi'])
         r[u][tmp.node[u]['pi']]['s.weight'] = tmp[u][tmp.node[u]['pi']]['s.weight']
   
   return r


def matriz_t(trail): 

   data = np.loadtxt(trail)
   rows, cols = np.where(data > 0)
   edges = zip(rows,cols)
   graf = nx.Graph(edges)

   for x,y in zip(rows, cols):
      graf[x][y]['weight'] = data[x][y]
      graf[x][y]['s.weight'] = data[x][y]
   return graf

   alemanha = matriz_adj("data/wg59_dist.txt")
   dijkstra_b = dijkstra(alemanha, [0, 42])
   dijkstra_c = dijkstra(alemanha, [0, 26, 53])


   draw(alemanha,True,"alemanha")
   draw(dijkstra_b,True,"dijkstra_b")
   draw(dijkstra_c,True,"dijkstra_c")


A = np.loadtxt('wg59_dist.txt')
G = nx.from_numpy_matrix(A)
nx.draw_networkx(G)
plt.savefig('inicial.pdf')
plt.show()


matriz_t(dijkstra(G,0))

nx.draw_networkx(newG)
plt.savefig('final.pdf')
plt.show()






