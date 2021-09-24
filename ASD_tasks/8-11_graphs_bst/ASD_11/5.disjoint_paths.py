#mamy znalezc liczbe rozłącznych wierzchołkowo ściezek z s do e
#w grafie skierowanym
#podaj algorytm znajdujący liczbe rozłącznych WIERZCHOŁKOWO ścieżek z s do e
#czyli nie mozna tego samego wierzchołka odwiedzic 2 razy

#kazdy wierzchołek u rozdzielam na dwa: u1 i u2
#dzieki temu zaden wierzcholek nie bedzie 2 razy odwiedzony
#u1 -do niego wchodzą te krawędzie co do u
#u2 - z niego wychodzą te krawędzie co z u
#kazda z krawędzi grafu otrzymuje przepustowosc 1
#a dla s oraz e ustalam przepustowosci inf(bo do nich wbiega i wybiega sporo sciezek)
#znajdujac max przepływ w grafie znajdziemy ilosc sciezek rozłącznych wierzchołkowo
#działa to poniewaz jak przez wierzchołek u puscimy sciezke to krawedz z u1 do u2 dostanie wartosc 0
#czyli juz w zadnej innej sciezce nie skorzystam z tego konkretnego wierzchołka u


#implementacja grafu o nowych wierzchołkach
#tworze nową macierz o rozmiarze 2 razy wiekszej niz wejsciowa
#kazdy wierzcholek v zostaje rozbity na: 2v oraz 2v+1
#wierzchołek 2v do niego wchodza krawedzie takie jak w oryginalnym v
#wierzcholek 2v+1 z niego wychodza krawedzie takie jak w oryginalnym v
#najpierw przechodze dwoma petlami - jesli dla jakis u i v
#znajduje sie krawedz w oryginalnym G to dodaje krawedz miedzy 2u+1 oraz 2v - odpowiada krawedzi tym w starym G
#przechodze liniowo po wartosciach i jak sie okaze ze v == s lub e to G1[2v][2v+1] = inf
#a w przeciwnym przypadku G1[2v][2v+1] = 1 - dodawanie krawedzi miedzy rozdzielonym wierzch v na dwie części

from queue import Queue

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


def fordFulkerson(G,s,e):
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


def disjointPaths(G,s,e):
    n = len(G)
    G1 = [[0] * (2*n) for _ in range(2*n)] #nowa macierz

    #kazdy wierzcholek v rodzielam na 2v i 2v + 1
    #wierzcholek 2v - do niego wychodzą kraeedzie do 2v+1
    #wierzchołek 2v+1 -z niego wychodzą krawędzie do kolejnych

    #wpisuje te krawędzie co były w oryginalnym G
    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                G1[2*u+1][2*v] = 1 #z 2u+1 wychodzi krawedz do 2v(bo w wejsciowej z u wychodziła krawędź do v)

    #miedzy wierzchołkiem rozdzielonym u na 2u i 2u+1 stawiam krawedz
    #wpisuje te krawędzie nowe które łączą rozdzielony wierzchołek
    for u in range(n):
        if u == s or u == e: #gdy u to wierzch startowy/koncowy
            G1[2*u][2*u + 1] = float("inf")
        else:
            G1[2*u][2*u+1] = 1 #krawędź łącząca rozbity wierzchołek u na u1(=2u) i u2(=2u+1)

    for i in G1:
        print(i)

    #2s- 1 z wierzchołków s(startowy)
    #2e+1- 2 z wierzchołków e(końcowy)
    return fordFulkerson(G1,2*s,2*e+1) #ilosc rozłacznych ścieżek

#inny sposob na rozdwajanie grafu
#gdy mam krawedz i->j
#to rozdzielam to na: i->i+n --> j->j+n
def disjointPath2(G,s,t):
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


G = [
    [0,1,0,1],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0],
]
print(disjointPath2(G,0,2))