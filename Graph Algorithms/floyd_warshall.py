#Algorytm Floyda-Warschalla
#Znajduje wszystkie najkrótsze ścieżki pomiedzy każdą parą wierzchołków w grafie ważonym.
#Wagi krawędzi mogą być zarówno dodatnie jak i ujemne, ale graf nie może posiadać ujemnych cykli.
#Złożoność: O(V^3)

#Implementacja dla reprezentacji macierzowej, zakłada, że graf nie posiada ujemnych cykli.

def floydWarshall(G):
    n = len(G)
    dist = G[:] #tablica odleglosci
    p = [[None] * n for _ in range(n)] #tablica parentow

    for k in range(n):
        for u in range(n): #startowy
            for v in range(n): #koncowy
                
                #0 - brak krawędzi
                if dist[u][v] == 0:
                    dist[u][v] = float("inf")
            
                #gdy poprzez wierzcholek k da sie 'taniej' dostac z u do v
                if dist[u][v] > dist[u][k] + dist[k][v]: 
                    dist[u][v] = dist[u][k] + dist[k][v] 
                    p[u][v] = k 

    return dist,p
