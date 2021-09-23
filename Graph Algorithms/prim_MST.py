#Algorytm Prima do znalezienia MST
#Implementacja dla list sąsiedztwa.

from queue import PriorityQueue

def prim(G):
    inf = float("inf")
    n = len(G)
    
    p = PriorityQueue()
    p.put((0,0))
    for i in range(1,n):
        p.put((inf,i))

    parents = [None] * n 
    visited = [False] * n
    min_weight = [inf] * n #min waga ktora prowadzi do parenta

    min_weight[0] = 0 

    while not p.empty():
        _, u = p.get() 
        visited[u] = True

        for edge,v in G[u]: 

            if not visited[v]:
                if min_weight[v] > edge:
                    min_weight[v] = edge
                    parents[v] = u
                    p.put((edge,v))

    MST = []
    for i in range(n):
        if parents[i] is not None:
            MST.append((parents[i],i,min_weight[i]))

    return MST
