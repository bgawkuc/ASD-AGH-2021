# Dany jest graf skierowany G = (V, E) oraz wierzchołki s i t. Proszę zaproponować algorytm 
# znajdujący maksymalną liczbę rozłącznych (wierzchołkowo) ścieżek między s i t.

#Graf wejściowy G jest rozmiaru n. Tworzę nowy graf G1 rozmiaru 2*n.
#Gdy w grafie G mam krawędź z u do v, to w G1 dodaje krawędź: z u do u+n, z u+n do v, z v do v+n.
#Dla grafu G1 szukam wartości maksymalnego przepływu, która wynosi tyle samo ilość rozłącznych ścieżek.

from queue import Queue

def BFS(G,s,t,parent):
    n = len(G)
    visited = [False] * n
    visited[s] = True

    q = Queue()
    q.put(s)

    while not q.empty():
        u = q.get()

        for v in range(n):
            if G[u][v] != 0 and not visited[v]:
                visited[v] = True
                parent[v] = u
                q.put(v)

    return visited[t]


def fordFulkerson(G,s,t):
    n = len(G)
    parent = [None] * n
    maxFlow = 0

    while BFS(G,s,t,parent):
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

#oblcza ilość rozłącznych ścieżek z s do t
def disjointPaths(G,s,t):
    n = len(G)
    newG = [[0] * (2*n) for _ in range(2*n)]

    #krawedź taka co w oryginalnym miedzy 2 wierzcholkami
    for i in range(n):
        for j in range(n):
            if G[i][j]:
                newG[i+n][j] = 1

    #krawedzie miedzy tym samym wierzcholkiem tylko ze rozdwojonym
    for i in range(n):
        if i == s or i == t:
            newG[i][i+n] = float('inf')
        else:
            newG[i][i+n] = 1

    return fordFulkerson(newG,s,t+n)
