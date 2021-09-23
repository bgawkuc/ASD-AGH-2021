#Algorytm Kruskala do znalezienia MST (minimalnego drzewa rozpinającego)
#Algorytm wykorzystuje strukturę find-union.
#Implementacja dla reprezentacji poprzez listy sąsiedztwa.

class Node:
    def __init__(self, idx):
        self.idx = idx
        self.parent = self 
        self.rank = 0


def findSet(x):
    if x != x.parent: 
        x.parent = findSet(x.parent) 
    return x.parent 


def union(x,y):
    x = findSet(x)
    y = findSet(y)

    if x.rank > y.rank:
        y.parent = x 

    elif y.rank > x.rank:
        x.parent = y

    else: =
        x.parent = y
        y.rank += 1 


def Kruskal(G):
    n = len(G)
    edges = []

    #dodaje krawędzie do tablicy edges
    for u in range(len(G)):
        for edge,v in G[u]:
            edges.append((edge,u,v))
    
    #sortuje po wartościcach krawędzi rosnąco
    edges.sort(key=lambda x: x[0])

    MST = []
    sets = [Node(i) for i in range(n)]
    
    #przechodzi po krawędziach i jeśli wierzchołki są w osobnych zbiorach (czyli nie ma połączenia między u a v) to dodaję krawędź do MST
    for edge,u,v in edges:
        if findSet(sets[u]) != findSet(sets[v]):
            MST.append((edge,u,v))
            union(sets[u],sets[v])

    return MST
