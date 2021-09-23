#BFS dla grafu ważonego
#Reprezentacja dla list sąsiedztwa
#Zlożoność: O(maxi*(V+E)), maxi-rozmiar największej krawędi
from queue import Queue

def BFS_false_vertex(G, u):
    n = len(G)
    q = Queue()
    visited = [False] * n
    dist = [None] * n

    # wierzcholek,ilosc sztucznych,rodzic,wartosc krawedzi
    q.put((u, 0, None, 0))
    visited[u] = True
    dist[u] = 0

    while not q.empty():
        u, cntFalse, parent, weight = q.get()
        if q.empty():
            q = Queue()

        # gdy zostały sztuczne wierzchołki
        if cntFalse > 0:
            q.put((u, cntFalse - 1, parent, weight))
        
        else:
            # gdy nie był jeszcze odwiedzony
            if not visited[u]:
                visited[u] = True

                if parent is None:
                    dist[u] = weight
                else:
                    dist[u] = weight + dist[parent]

            # wrzucam do kolejki wszystkie jego dzieci które nie były odwiedzone
            for v, edge in G[u]:
                if not visited[v]:
                    q.put((v, edge - 1, u, edge))
    return dist
