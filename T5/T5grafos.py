import numpy as np
import networkx as nx
from heapq import heappop, heappush
pop = heappop
push = heappush

def twice_around(G, origin = 0):                
    H = nx.minimum_spanning_tree(G)                     # Encontra a MST de G
    H = nx.MultiGraph(H)   
    for u,v in H.edges():                               # Duplica as arestas da MST
        H.add_edge(u,v) 

    euleraux = list(nx.eulerian_circuit(H, origin))     # Encontra circuito Euleriano
    I = nx.Graph()
    aux = []
    for u,v in euleraux:                                # Adiciona em aux todos os vertices do circuito Euleriano
        aux.append(u)
        aux.append(v)
    h = []
    for i in aux:                                       # Adiciona os h os vértices de aux sem repeticoes
        if (i not in h):
            h.append(i)
    h.append(origin)                                    # Adiciona a origem
    for i in range (30):                                # Coloca em
        I.add_edge(h[i],h[i+1])
        I[h[i]][h[i+1]]['weight'] = G[h[i]][h[i+1]]['weight']    
    return I                                            # Retorna I
    
def calcula_peso(T): 
    peso = 0
    pesos = nx.get_edge_attributes(T, 'weight')
    for v in T.edges(): 
        peso += pesos[v]
    return peso
        
# Main
A = np.loadtxt('ha30_dist.txt')
G = nx.from_numpy_matrix(A)
min_pesos = []
max_pesos = []
for i in range(30):
    H = twice_around(G, i)
    weight = calcula_peso(H)
    push(min_pesos, (weight, i))
    push(max_pesos, (-weight, i))

for i in range(3): 
    peso, inicial = pop(min_pesos)
    print("Iniciando em ", inicial, ":", peso)

for i in range(3): 
    peso, inicial = pop(max_pesos)
    print("Iniciando em ", inicial, ":", -peso)

pos = nx.spring_layout(H, k = 0.35, iterations=100)
nx.draw_networkx(H, pos)