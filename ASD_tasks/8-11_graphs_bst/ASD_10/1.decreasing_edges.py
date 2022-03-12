# Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru {1, . . . , ∣E∣} (wagi krawędzi są parami różne).
# Proszę zaproponować algorytm, który dla danych wierzchołków x i y oblicza ścieżkę o najmniejszej sumie wag,
# która prowadzi z x do y po krawędziach o malejących wagach (jeśli ścieżki nie ma to zwracamy ∞).

# Graf jest reprezentowany jako tablica wypełniona 3-elementowymi tablicami: [u,v,edge].
# u,v-wierzcholki, edge - wartość krawędzi pomiędzy nimi

from math import inf   

def decreasing(G,s,t,n):
    G.sort(key=lambda x: x[2], reverse=True)
    
    dist = [inf] * n
    parent = [None] * n
    dist[s] = 0
    
    for u,v,edge in G:
        if dist[v] > dist[u] + edge:
            dist[v] = dist[u] + edge
            parent[v] = u

    path = []

    curr = t
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    
    if dist[t] < inf:
        return path[::-1], dist[t]
    return inf