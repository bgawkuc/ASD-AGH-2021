#znajdź max skojarzenie w drzewie(graf nieskierowany,acykliczny)

#drzewo jest grafem dwudzielnym
#więc mozna uzyc algorytmu do znajdowania max skojarzenia w grafie dwudzielnym
#ale najpierw musze go przerobic na graf dwudzielny skierowany
#w którym krawędzie prowadzą tylko z lewego zbioru(A) do prawego(B)
#wywołuje BFS do kolorowania wierzchołków i dzieki temu mamy wierzcholki koloru 1 i 0
#ustalam sobie ze bede prowadzic krawędzie skierowane z wierzchołków o kolorze "1" do wierzchołków koloru "0"
#tworze graf o 2 większy niz rozmiar grafu wejściowego
#te 2 dodatkowe wierzchołki to będzie super-źródło i super-ujście
#i teraz moge zaczac przepisywać krawędzie do nowego grafu
#jak miedzy u a v jest krawędź w wejsciowym
#oraz u jest w grupie koloru 1 a v w grupie koloru 0
#to dodaje krawędź z u do v oraz dodatkowo:
#1) z super źródla do u
#2) z v do super ujścia
#kazda krawędź ma wagę 1
#i na takim nowym grafie mogę wywołać juz algorytm do znajdowania max przepływu
#max skojarzeniem będzie max flow od super zrodła do super ujścia

from queue import Queue

#BFS do maxflow
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

#BFS do okreslenia kolorowania wierzchołków
def BFS2(G,s):
    q = Queue()
    visited = [False] * len(G)
    color = [-1] * len(G)

    q.put(s)
    visited[s] = True
    color[s] = 1  # 1 kolor

    while not q.empty():
        u = q.get()

        for v in range(len(G)):
            if u != v and G[u][v] == 1 and not visited[v]:
                visited[v] = True
                color[v] = 1 - color[u]  # jego dziecko koloruje na kolor inny
                q.put(v)

            if G[u][v] == 1 and u != v and color[u] == color[v]:  # gdy kolor dziecka i rodzica jest ten sam
                return False

    return color #zwraca tablice z pokolorowanymi wierzchołkami na dwa kolory 0 i 1


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


def maxMatchingTree(G):
    n = len(G)
    G1 = [[0] * (n+2) for _ in range(n+2)] #nowy graf z 2 wierzchołkami wiecej

    s = n #super-źródło
    e = n + 1 #super-ujście

    color = BFS2(G,0) #podział na wierzchołki z A i B, A-mają kolor 1,B-mają kolor 0
    print(color)

    for u in range(n):
        for v in range(n):

            #warunek by wierzchołek u był w lewym zbiorze(A)
            #a wierzchołek v w prawym zbiorze(B)
            #prowadze wtedy krawędź skierowaną z u do v
            #oraz z s do u i z v do e
            if G[u][v] == 1 and color[u] == 1 and color[v] == 0:
                G1[u][v] = G[u][v]
                G1[s][u] = 1 #krawędź z super-źródła do u
                G1[v][e] = 1 #krawędź z v do super-ujścia

    for i in range(n+2):
        print(G1[i])

    return fordFulkerson(G1,s,e) #max skojarzenie to max flow z super źródła do super ujścia


G = [[0] * 8 for _ in range(8)]
G[0][1] = 1
G[1][0] = 1
G[1][2] = 1
G[2][1] = 1
G[2][4] = 1
G[4][2] = 1
G[2][3] = 1
G[3][2] = 1
G[4][5] = 1
G[5][4] = 1
G[5][6] = 1
G[6][5] = 1
G[5][7] = 1
G[7][5] = 1


print(maxMatchingTree(G))