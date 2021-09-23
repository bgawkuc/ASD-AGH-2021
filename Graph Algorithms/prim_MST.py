#algorytm Prima do znajdowania MST
#minimalne drzewo rozpinajace
#wybieram sobe woerzcholek s od ktorego zaczynam

#algorytm
#wrzucam do kolejki wszystkie wierzcholki z wart inf
#a startowy z wartoscia 0
#tworze tablice:
#parent - rodzic wierzch
#visited - czy odwiedzony
#min_weight - waga krawedzi ktora laczy wierzch z rodzicem

#dopoki kolejka nie będzie pusta:
#wyjmuje wierzchołek
#zaznaczam go jako odwiedzony
#patrze na jego dziecko v
#jesli nie bylo odwiedzone to sprawdzam wartosc min_weight[v]
#jesli min_weight[v] > obecnej krawedzi z u do v
#to min_weigh[v] ustawiam na krawedz z u do v
#to wsadzam do kolejki (krawedz z u do v, v)
#ustawiam rodzica v na u

#i na koncu liniowo przechde po rodzicacg
#jak jakis wierzch ma rodzica != None
#to krawedz miedzy rodzicem a wierzchołkiem nalezzy do MST

from queue import PriorityQueue

def prim(G,s):
    p = PriorityQueue()
    inf = float("inf")
    n = len(G)

    #wszystkie wierzcholki wrzucam z waga inf poza startowym ktory dostaje 0
    for i in range(n):
        if i != s:
            p.put((inf,i))
        else:
            p.put((0,i))

    parents = [None] * n #rodzic
    visited = [False] * n
    min_weight = [inf] * n #min waga ktora prowadzi do parenta

    min_weight[s] = 0 #wierzcholek startowy sam jest swoim parentem

    while not p.empty():
        _, u = p.get() #wyjmuje wierzch u
        visited[u] = True #odznaczam go jako odwiedzony

        for edge,v in G[u]: #patrze na jego dzieci

            if not visited[v]:
                if min_weight[v] > edge: #gdy obecna waga dla wierzch v jest wieksza od wart krawedzi z u do v(weightv)
                    min_weight[v] = edge #aktualizuje min wage
                    parents[v] = u
                    p.put((edge,v))

    MST = []
    for i in range(n):
        if parents[i] is not None:
            MST.append((parents[i],i,min_weight[i]))

    return MST

#(wartosc krawedzi, wierzcholek do ktorego krawedz prowadzi)
G = [
    [[7,1],[1,2],[1,3]],
    [[7,0],[6,2],[1,4]],
    [[1,0],[6,1],[7,3]],
    [[1,0],[7,2],[7,4]],
    [[1,1],[7,3]],
]
print(prim(G,0))