#najwieksze skojarzenie grafu
#to taki zbior krawedzi ze zadna z nich nie dzieli wierzchołka z inną
#reprezentacja macierzowa

#1 sposób
#wywoluje DFS dla kazdego wierzcholka w grafie
#jesli znajduje sie wsrod niego i reszty wierzcholkow krawędź to sprawdzam
#czy nie był odwiedzony
#jesli nie to zapisuje z jakim wierzcholkiem tworzy on krawedź w skojarzeniu
#i jesli takie cos zaszlo tzn ze dlg skojareznia zwiekszam o 1
#a gdyby byl juz w edge jakis odhaczony wierzch to sprawfzam czy to nie ten z którym mam skojarzenie
#bo jak jest ten sam to zapisuje go w edge
#na koncu dziele wynik na 2 bo krawędzie skojarzone odwiedzałam 2 razy

def DFS(G):
    n = len(G)
    edge = [None] * n
    res = 0

    def DFSvisit(u):

        for v in range(n):

            if G[u][v] and not visited[v]:
                visited[v] = True

                if edge[v] == None or DFSvisit(edge[v]):
                    edge[v] = u
                    return True
        return False


    for u in range(n):
        visited = [False] * n

        if DFSvisit(u):
            res += 1

    # print(edge)
    return res

#2 sposób
#na wejsciu jest graf dwudzielny ale nieskierowany!!
#musze wyroznic w nim zbiory A oraz B by prowadzic tylko krawędzie skierowane z A do B
#max skojarzenie mozna wyznaczyc poprzez dodanie super-źródła i super-ujścia
#i załozenie ze kazda krawędź ze zbioru A jest skierowana do zbioru B
#a jej przepustowość wynosi 1
#super źródło ma krawędź do wierzchołków z A
#wierzchołki z B mają krawędź do super ujścia
#max skojarzeniem jest max przepływ od super-źródła do super-ujścia
#poniewaz ten max flow to max ilosc sciezek gdy wszystkie krawędzie mają wartosc 1

#algorytm dla skierowanego
from queue import Queue

#BFS uzyty do maxflow
def BFS(G,s,e,parent):
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

    return visited[e]


def fordFlukerson(G,s,e):
    n = len(G)
    parent = [None] * n
    maxFlow = 0

    while BFS(G,s,e,parent):
        u = e
        mini = float("inf")

        while u != s:
            if G[parent[u]][u] < mini:
                mini = G[parent[u]][u]
            u = parent[u]

        maxFlow += mini

        u = e
        while u != s:
            G[parent[u]][u] -= mini
            G[u][parent[u]] += mini
            u = parent[u]

    return maxFlow

def colorBfs(G,s):
    n = len(G)
    visited = [False] * n
    color = [-1] * n
    q = Queue()

    color[s] = 1
    visited[s] = True
    q.put(s)

    while not q.empty():
        u = q.get()

        for v in range(n):
            edge = G[u][v]
            if edge > 0 and u != v:
                if not visited[v]:
                    color[v] = 1 - color[u]
                    visited[v] = True
                    q.put(v)
                else:
                    if color[v] == color[u]:
                        return False
    return color

def maxMatching(G):
    n = len(G)
    G1 = [[0] * (n+2) for _ in range(n+2)]
    color = colorBfs(G,0) #dwie grupy kolor: 1 i 0

    s = n #super źródło
    e = n + 1 #super ujście

    for u in range(n):
        for v in range(n):

            # gdy jest krawędź w grafie wejsciowym z u do v
            #a wierzcholki u,v naleza do roznych grup kolorow
            #(warunek ze graf jest dwudzielny)
            #to dodaje krawędź z super źródła do u oraz z v do super ujscia
            #czyli teraz mam: super-źródlo->u->v->super-ujście
            if G[u][v] == 1 and color[u] == 1 and color[v] == 0:
                G1[u][v] = 1
                G1[s][u] = 1
                G1[v][e] = 1

    return fordFlukerson(G1,s,e) #szukam wartosci max przepływu = max skojarzenie




g = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1]]

g1 = [
    [0,0,0,1,1,1],
    [0,0,0,1,0,1],
    [0,0,0,1,1,0],
    [0,1,1,0,0,0],
    [1,0,1,0,0,0],
    [1,1,0,0,0,0],
]


# print(DFS(g1))
print(maxMatching(g1))
