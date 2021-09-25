# Proszę podać algorytm, który mając na wejściu drzewo oblicza skojarzenie o maksymalnej liczności.

#Drzewo jest grafem dwudzielnym. Za pomocą BFS znajduje dwie grupy wierzchołków (kolorów), który taki graf tworzą.
#Tworzę nowy graf G1 z 2 dodatkowymi wierzchołkami - super źródłem i super ujściem.
#W grafie G1 dodaje te same krawędzie co były w drzewie oraz gdy wierzhcołek należy do koloru 0 to dodaje krawędź 
#z super źródła do niego. Jeśli należał on do koloru 1 to dodaje krawędź z niego do super ujścia.
#Wartość maksymalnego przepływu z super źródła do super ujścia stanowi wartość skojarzenia o maksymalnej liczności. 

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


def maxMatchingTree(G):
    n = len(G)
    G1 = [[0] * (n+2) for _ in range(n+2)] #nowy graf z 2 wierzchołkami wiecej

    s = n #super-źródło
    t = n + 1 #super-ujście

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

    return fordFulkerson(G1,s,t) #max skojarzenie to max flow z super źródła do super ujścia
