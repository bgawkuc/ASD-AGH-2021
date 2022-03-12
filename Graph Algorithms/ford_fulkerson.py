# Algorytm Forda-Fulkersona znajdujący maksymalny przeplyw w grafie od wierzchołka s do t.

# Implementacja dla reprezentacji macierzowej.
from queue import Queue


# BFS, który sprawdza czy istnieje ścieżka z s do t i aktualizuje tablice parent
def BFS(G, s, t, parent):
    n = len(G)
    visited = [False] * n

    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        u = q.get()

        for i in range(n):
            # 0-brak krawędzi
            if G[u][i] != 0 and not visited[i]:
                parent[i] = u
                visited[i] = True
                q.put(i)

    return visited[t]


def fordFulkerson(G, s, t):
    n = len(G)
    parent = [False] * n
    maxFlow = 0

    # dopóki istnieje ścieżka z s do t
    while BFS(G, s, t, parent):
        u = t
        mini = float("inf")

        # szukam najmniejszej krawędzi na ścieżce z s do t
        while u != s:
            mini = min(mini, G[parent[u]][u])
            u = parent[u]

        # wartość przepływu zwiększam o wagę najmniejszej krawędzi na ścieżce z s do t
        maxFlow += mini

        u = t

        # aktualizuje wartosci krawędzi
        while u != s:
            G[parent[u]][u] -= mini
            G[u][parent[u]] += mini
            u = parent[u]

    return maxFlow
