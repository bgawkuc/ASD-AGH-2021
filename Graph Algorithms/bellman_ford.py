#Algorytm Bellmana-Forda
#Oblicza najkrótszą ścieżke w grafie ważonym, skierowanym.
#Dopuszcza ujemne krawędzie (o ile nie występują ujemne cykle).
#Implementacja dla list sąsiedztwa.
#Złożoność: O(V*E)

def bellmanFord(G, s):
    inf = float("inf")
    n = len(G)

    dist = [inf] * n
    parent = [None] * n
    dist[s] = 0

    for _ in range(n - 1):  
        for u in range(n): 
            for edge, v in G[u]:

                #relaksacja
                if dist[v] > dist[u] + edge:
                    dist[v] = dist[u] + edge
                    parent[v] = u

    #weryfikacja - sprawdza czy graf nie zaweira ujemnych cykli
    for u in range(n):
        for edge,v in G[u]:

            #gdyby wynik zaczał sie poprawiac tzn ze trafiłam na ujemny cykl
            if dist[v] > dist[u] + edge:
                return False

    return dist, parent
