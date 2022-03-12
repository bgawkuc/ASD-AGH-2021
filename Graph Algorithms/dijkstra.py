# Algorytm Dijkstry - szuka najkrótszych ścieżek w grafie o nieujmenych wagach krawędzi.
# Dwa rodzaje implementacji:
# 1) z kolejką priorytetową dla reprezentacji przez listy sąsiedztwa - O(ElogV)
# 2) bez kolejki priorytetowej dla reprezentacji macierzowej - O(V^2)

# 1)Implementacja dla list sąsiedztwa
# Złożoność: O(ElogV)
from queue import PriorityQueue


def dijkstra(G, s, t):
    n = len(G)
    inf = float("inf")

    parents = [None] * n
    visited = [False] * n
    p = PriorityQueue()

    # wkładam do kolejki krotki: (odległość,wierzchołek)
    p.put((0, s))
    dist = [inf] * n
    dist[s] = 0

    while not p.empty():
        _, u = p.get()
        visited[u] = True

        for v, edge in G[u]:

            # relaksacja
            if dist[v] > dist[u] + edge and not visited[v]:
                dist[v] = dist[u] + edge
                parents[v] = u
                p.put((dist[v], v))

    curr = t
    path = []
    while curr is not None:
        path.append(dist[curr])
        curr = parents[curr]

    # zwraca minimalną ścieżkę z s do t i jej długość
    return path[::-1], dist[t]


# 2)Implementacja dla reprezentacji macierzowej
# Złożoność: O(V^2)

# szuka wierzchołka, o minimalnej wartości dist, który nie był jeszcze odwiedzony
def getMinVertex(visited, dist):
    v = None

    for i in range(len(dist)):
        if not visited[i] and (v is None or dist[v] > dist[i]):
            v = i
    return v


def dijkstra2(G, s, t):
    n = len(G)
    inf = float("inf")

    parent = [None] * n
    visited = [False] * n
    dist = [inf] * n
    dist[s] = 0

    for _ in range(n):
        u = getMinVertex(visited, dist)
        if u is None:
            break
        visited[u] = True

        for v in range(n):
            edge = G[u][v]

            # 0 - oznacza brak krawędzi
            if edge != 0:
                if not visited[v] and dist[v] > dist[u] + edge:
                    dist[v] = dist[u] + edge
                    parent[v] = u

    curr = t
    path = []
    while curr is not None:
        path.append(dist[curr])
        curr = parent[curr]

    # najkrótsza ściezka z s do t oraz jej długość
    return path[::-1], dist[t]
