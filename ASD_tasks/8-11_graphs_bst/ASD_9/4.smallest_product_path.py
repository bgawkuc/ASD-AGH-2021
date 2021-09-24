# Mamy dany graf G = (V, E) z wagami w∶ E → N−{0} (dodatnie liczby naturalne).
# Chcemy znalezc scieżkę z wierzchołka u do v tak, by iloczyn wag był minimalny


#Wykonujemy zwykły algorytm dijkstry, z różnicą, że będą brane wartości logarytmów krawedzi.
#Dzięki temu minimalizujac sumę logarytmów, zminimalizujemy iloczyn krawędzi.
#log(x) + log(y) = log(xy)


from queue import PriorityQueue
from math import log10

def Dijkstra(G,s,t):
    n = len(G)
    inf = float("inf")

    parent = [None] * n
    visited = [False] * n
    dist = [inf] * n
    dist[s] = 0

    q = PriorityQueue()
    q.put((0,s))
    
    while not q.empty():
        _, u = q.get()
        visited[u] = True
        for edge,v in G[u]:
            
            #relaksacja, rozważam logarytm z wagi krawędzi
            if not visited[v] and dist[v] > dist[u] + log10(edge):
                dist[v] = dist[u] + log10(edge)
                parent[v] = u
                q.put((dist[v],v))

    path = []
    last = t
    
    while last != None:
        path.append(last)
        last = parent[last]

    return path[::-1]
