# Proszę wskazać algorytm, który znajduje maksymalny przepływ między źródłem i ujściem w grafie nieskierowanym.

# Graf wejściowy G (rozmiaru n) należy przerobić na graf skierowany, dla którego należy użyć algorytmu Forda-Fulkersona na największy przepływ.
# Liczę ilość krawędzi w grafie G i tworzę nowy graf G1 rozmiaru n+ilość krawędzi.
# Dla każdej grawędzi z u do v w G tworzę krawędź skierowaną z u do v i v do nowego wierzcholka i z nowego wierzchołka do u w G1.
# Dla grafu G1 liczę maksymalny przepływ.

from queue import Queue


def BFS(G, s, t, parent):
    n = len(G)
    visited = [False] * n
    visited[s] = True

    q = Queue()
    q.put(s)

    while not q.empty():
        u = q.get()

        for i in range(n):
            if G[u][i] != 0 and not visited[i]:
                visited[i] = True
                parent[i] = u
                q.put(i)

    return visited[t]


def fordFulkerson(G, s, t):
    n = len(G)
    parent = [None] * n
    maxFlow = 0

    while BFS(G, s, t, parent):
        u = t
        mini = float("inf")

        while u != s:
            if G[parent[u]][u] < mini:
                mini = G[parent[u]][u]
            u = parent[u]

        maxFlow += mini

        u = t
        while u != s:
            G[parent[u]][u] -= mini
            G[u][parent[u]] += mini
            u = parent[u]
    return maxFlow


def maxFlowUndirected(G, s, t):
    cntEdges = 0
    n = len(G)

    # zliczam ilosc krawedzi w G
    for i in range(n):
        for j in range(n):
            if i < j and G[i][j] != 0:
                cntEdges += 1

    m = n + cntEdges
    G1 = [[0] * m for _ in range(m)]
    newVertex = n

    for u in range(n):
        for v in range(n):
            if u < v and G[u][v] != 0:
                G1[u][v] = G[u][v]
                G1[v][newVertex] = G1[newVertex][u] = G[u][v]
                newVertex += 1

    return fordFulkerson(G1, s, t)
