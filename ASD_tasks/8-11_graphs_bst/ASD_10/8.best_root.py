# Dany jest acykliczny, spójny nieskierowany, ważony graf T (czyli T jest tak naprawdę ważonym drzewem).
# Proszę wskazać algorytm, który znajduje taki wierzchołek T, z którego odległość do najdalszego wierzchołka jest minimalna.

# Szukam średnicy drzewa (największej ścieżki - pod względem sumy wag) za pomocą 2-krotnego wywołania DFS.
# W średnicy szukam wierzchołka, który podzieli ją na 2 częsci o minimalnej różnicy.

def dfs(G, s):
    n = len(G)
    visited = [False] * n
    dist = [-1] * n
    dist[s] = 0
    parent = [None] * n

    def dfsVisit(u):
        visited[u] = True

        for v, edge in G[u]:
            if not visited[v]:
                dist[v] = dist[u] + edge
                parent[v] = u
                dfsVisit(v)

    dfsVisit(s)
    return dist, parent


def bestRoot(G):
    n = len(G)
    d1, _ = dfs(G, 0)

    # szukam wierzcholka u - najbardziej oddalonego od 0
    u = 0
    for i in range(1, n):
        if d1[i] > d1[u]:
            u = i

    d2, parent = dfs(G, u)
    print(d2)

    # szukam wierzcholka v - najbardziej oddalonego od u
    v = u
    for i in range(n):
        if d2[i] > d2[v]:
            v = i

    length = d2[v]
    path = []
    curr = v
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    path = path[::-1]

    root = u
    diff = length

    # szukam najlepszego wierzcholka
    # czyli takiego wierzchołka który dzieli srednice na 2 czesci o min roznicy
    for u in path:
        left = d2[u]
        right = length - left
        if abs(left - right) < diff:
            diff = abs(left - right)
            root = u

    return diff, root
