#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as n
import matplotlib.pyplot as plt
from BFS import BFS                 # Importa método BFS

# Cria grafo G
G = nx.Graph()

# Coloca os valores de karate.paj em G
G = nx.read_pajek('karate.paj')

# Chama método que retorna a BFS-tree
H = BFS(G, '1')

# Salva as profundidades cada nó de H em labels
labels = {}
for v in H.nodes():
    labels[v] = H.node[v]['depth']

# Retorna um dicionário de posições codificadas por nó
pos = nx.spring_layout(H)

# Desenha o grafo H
nx.draw(H, pos)

# Desenha com as arestas e labels
nx.draw_networkx_labels(H, pos, labels)
nx.draw_networkx_edges(H, pos)

# Exibe
plt.show()
