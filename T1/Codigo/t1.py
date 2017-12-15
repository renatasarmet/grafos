import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#CARREGANDO A MATRIZ DE ADJACÊNCIAS 
A = np.loadtxt('matriz.txt')

#CRIANDO UM GRAFO A PARTIR DA MATRIZ CARREGADA
G = nx.from_numpy_matrix(A)

#RENOMEANDO OS VÉRTICES DO GRAFO
labels = {}
for i in range(0, 36):
     labels[i] = i + 1

H = nx.relabel_nodes(G,labels)

#CARREGANDO O ARQUIVO CONTENDO O VETOR DE PROBABILIDADES INICIAL 
p_atual = np.loadtxt('vetor.txt')

for i in range (0, 100):
     #MULTIPLICA A MATRIZ DE ADJACÊNCIAS PELO VETOR DE PROBABILIDADES
     p_atual = np.dot(p_atual, A)
     
print("PROBABILIDADE DE ALCANÇAR CADA VERTICE (ESTADO) EM 100 JOGADAS")
for i in range(0, 36):
     print(i + 1, p_atual[i])

#CRIANDO A MATRIZ P_
P_ = nx.google_matrix(G, alpha=0.1)

#REALIZANDO O PAGERANK
w = nx.pagerank(G, alpha=0.1, max_iter=100)
W = [0.for i in range(len(P_))]

for key in w:
     W[key-1]= w[key]

#COMPARANDO O RESULTADO DO PAGERANK COM O RESULTADO DO POWERMETHOD
diferente = False # booleana para diferentes

for i in range(len(p_atual)):
     if(p_atual[i] != W[i]):
          diferente = True 

if(diferente):
    print("\nSão diferentes.")
else:
     print("\nSão iguais.")

#PRINTA O DIAGRAMA DE ESTADOS QUE REPRESENTA O JOGO
pos = nx.spring_layout(H)
nx.draw(H, pos, with_labels=True)
plt.show()

