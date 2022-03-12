# Sortowanie topologiczne dla grafu skierowanego.
# Ustala kolejność wierzchołków w ten sposób, by każdy wierzchołek znajdował się przed wierzchołkami,
# do których prowadzą krawędzie z niego wychodzące.
# Implementacja dla reprezentacji przez listy sąsiedztwa.

def DFS(G):
    order = []
    visited = [False] * len(G)

    def DFSvisit(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFSvisit(v)

        order.append(u)

    for u in range(len(G)):
        if not visited[u]:
            DFSvisit(u)

    return order[::-1]
