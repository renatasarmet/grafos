#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as n

# Criando estrutura de pilha para ser utilizada
class Pilha(object):
    def __init__(self):
        self.dados = []
 
    def empilha(self, elemento):                            # Método para empilhar
        self.dados.append(elemento)                         # Adiciona no final do vetor de dados
 
    def desempilha(self):                                   # Método para desempilhar
        if not self.vazia():                                # Verifica se a pilha não está vazia
            return self.dados.pop(-1)                       # Se não estiver, retira o último elemento do vetor (último a entrar)
 
    def vazia(self):                                        # Método para verificar se a pilha está vazia
        return len(self.dados) == 0                         # Se o tamanho do vetor de dados for zero, então está vazia

# Algoritmo de Busca em Profundidade
def DFS(G, s):
    cor  = {}                                               # Cores indicando disponivel/ na pilha/ completado
    pred = {}                                               # Predecessores
    d    = {}                                               # Distância

    for v in G.nodes():                                     # Para todos os nós do grafo G
        d[v]    = n.inf                                     # Inicializa todas as distâncias com infinito
        cor[v]  = 'branco'                                  # Branco, cinza e preto. Inicializa todos com branco (disponíveis)
        pred[v] = None                                      # Inicializa todos os predecessores com nulo

    cor[s]  = 'cinza'                                       # Cinza = na pilha

    p = Pilha()                                             # Cria Pilha p
    p.empilha(s)                                            # Colocado na pilha

    while not p.vazia():                                    # Enquanto a pilha não estiver vazia
        u = p.desempilha()                                  # Desempilha
        if pred[u] == None:                                 # Se for o primeiro nó (raiz)   
            d[u] = 0                                        # Inicializa distância com 0
        else:                                               # Se não, se for qualquer outro nó
            d[u] = d[pred[u]] + 1                           # Atualiza a distância dele para a distância do predecessor + 1

        for v in G.neighbors(u):                            # Para todos os vizinhos de u
            if cor[v] == 'branco' or cor[v] == 'cinza':     # Se o nó ainda estiver disponível ou na pilha
                cor[v]  = 'cinza'                           # Garante que a cor indicará que está na pilha
                pred[v] = u                                 # Coloca u como predecessor

                p.empilha(v)                                # Adiciona na pilha

        cor[u] = 'preto'                                    # Depois de checado todos os vizinhos de u, marca ele como completado

    H = nx.create_empty_copy(G)                             # Cria uma cópia de G com todas as arestas removidas

    for v1,v2 in G.edges():                                 # Retorna as arestas de v1 e v2 presentes em G, com default data {}

        if (pred[v2] is v1) or (pred[v1] is v2 and not nx.is_directed(H)):  #Se o predecessor de v2 for v1 ou se o predecessor de v1 for v2 e não for um grafo direcional
            
            H.add_edge(v1, v2)                              # Adiciona essa aresta em H
            H.node[v1]['depth'] = d[v1]                     # Adiciona o atributo profundidade em v1 com a distância salva dele
            H.node[v2]['depth'] = d[v2]                     # Adiciona o atributo profundidade em v2 com a distância salva dele

    return H                                                # Retorna o grafo H com a BFS-tree
