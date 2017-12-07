#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as n

# Algoritmo de Busca em Largura
def BFS(G, s):
    cor  = {}                           # Cores indicando disponivel/ na fila/ completado
    pred = {}                           # Predecessores
    d    = {}                           # Distância

    for v in G.nodes():                 # Para todos os nós do grafo G
        d[v]    = n.inf                 # Inicializa todas as distâncias com infinito
        cor[v]  = 'branco'              # Branco, cinza e preto. Inicializa todos com branco (disponíveis)
        pred[v] = None                  # Inicializa todos os predecessores com nulo

    cor[s]  = 'cinza'                   # Cinza = na fila
    d[s]    = 0                         # Nó de origem tem distância zero

    Q = [ s ]                           # Colocado na fila

    while Q:                            # Enquanto a fila não estiver vazia
        u = Q.pop(0)                    # Retira o primeiro da fila
        for v in G.neighbors(u):        # Para todos os vizinhos de u
            if cor[v] == 'branco':      # Se o nó ainda estiver disponível
                cor[v]  = 'cinza'       # Muda a cor para indicar que está na fila
                d[v]    = d[u] + 1      # Atualiza a distância dele para a distância de u + 1
                pred[v] = u             # Coloca u como predecessor

                Q.append(v)             # Adiciona na fila

        cor[u] = 'preto'                # Depois de checado todos os vizinhos de u, marca ele como completado

    H = nx.create_empty_copy(G)         # Cria uma cópia de G com todas as arestas removidas

    for v1,v2 in G.edges():   # Retorna as arestas de v1 e v2 presentes em G, com default data {}
        if (pred[v2] is v1) or (pred[v1] is v2 and not nx.is_directed(H)):  #Se o predecessor de v2 for v1 ou se o predecessor de v1 for v2 e não for um grafo direcional
            H.add_edge(v1, v2)        # Adiciona essa aresta em H
            H.node[v1]['depth'] = d[v1]     # Adiciona o atributo profundidade em v1 com a distância salva dele
            H.node[v2]['depth'] = d[v2]     # Adiciona o atributo profundidade em v2 com a distância salva dele

    return H                            # Retorna o grafo H com a BFS-tree
