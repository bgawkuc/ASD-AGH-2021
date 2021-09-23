#Algorytm mostów- znajduje wszystkie mosty w grafie (reprezentacja przez listy sąsiedztwa).
#Most - krawędź, która rozspójnia graf.
#Złożoność: O(V+E)


def DFS(G):
    time = 0
    n = len(G)
    bridges = []
    visited = [False] * n
    parents = [None] * n
    d = [0] * n #czas dotarcia do wierzcholka poprzez użycie DFS
    l = [0] * n #najmniejszy mozliwy czas dotarcia do wierzchołka (różny od d[i] gdy wystąpi krawędź wsteczna)

    def DFSvisit(u): 
        nonlocal time
        time += 1
        d[u] = l[u] = time
        visited[u] = True

        for v in G[u]:

            if not visited[v]:
                parents[v] = u
                visited[v] = True
                DFSvisit(v)

                l[u] = min(l[u],l[v]) 
            
            elif visited[v] and parents[u] != v:
                l[u] = min(l[u], d[v])


    for u in range(n):  
        if not visited[u]:
            DFSvisit(u)

    for u in range(n):
        if d[u] == l[u] and parents[u] != None:
            bridges.append((parents[u],u))

    return bridges
