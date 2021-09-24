#mam graf nieksierowany spójny
#spojnosc krawedziowa k to ilosc k krawedzi którą nalezy usunac by rozspojnic graf

#graf trzeba przerobic na graf skierowany by dało sie w nim uzyc algorytm na max przepływ
#(algorytm z dodatkowymi wierzchołkami)
#a nastepnie puścic algorytm forda fulkersona dla dowolnego wierzchołka tylko ze |v| - 1 razy(do kazdego innego)
#szukam najmniejszej wartosci z maxflow jakie mi on zwróci
#i to bedzie moja odpowiedź -> k
#kazda krawędź dostaje wage 1

#puszczam od wierzcholka 0 do kazdego innego
#algorytm forda-flukersona liczy mi ilosc sciezek z 0 do i-tego wierzcołka
#i szukam po tych ilosciach tej najmniejszej
#bo jak usune tyle krawędzi co wynosi min ilosc sciezek dla jakiegos wierzchołka to rozspojnie ten wierzchołek
#usuwam te krawędxie które wchodziły do i-tego wierzchołka
#bo wiem ile sciezek do niego wchodzi
#wiec jak zabiore wszystkie krawedzie wchodzace do i-tego wierzch(<=>ilośc sciezek) to rozspojnie ten wierzchołek(i-ty)
#wierzchołek z którego puszczam algorytm mogę wybrać losowo i to zadzaiała
#bo znajdzie on ilosc sciezek od wybranego wierzcholka do kazdego innego
#O(V^2E^2) bo ford-fulkerson ma VE^2 a puszczam go V-1 razy

from queue import Queue
def BFS(G,s,e,parent):
    n = len(G)
    visited = [False] * n
    visited[s] = True

    q = Queue()
    q.put(s)

    while not q.empty():
        u = q.get()
        for i in range(n):
            if G[u][i] != 0 and not visited[i]:
                visited[i] = True
                parent[i] = u
                q.put(i)

    return visited[e]

#szuka max przepływu w grafie skierowanym
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

#szuka max przepływu w grafie nieskierowanym
def maxFlowUndirected(G,s,e):
    n = len(G)
    cntEdges = 0

    for u in range(n):
        for v in range(n):
            if u < v and G[u][v] != 0:
                cntEdges += 1

    m = n + cntEdges #rozmiar nowego grafu
    G1 = [[0] * m for _ in range(m)]
    newVertex = n #nowy wierzchołek

    for u in range(n):
        for v in range(n):
            if u < v and G[u][v] != 0:
                G1[u][v] = G[u][v]
                G1[v][newVertex] = G1[newVertex][u] = G[u][v]
                newVertex += 1
    return fordFulkerson(G1,s,e)


def edgeConnectivity(G):
    n = len(G)
    s = 0
    k = float("inf")

    #puszczam szukanie max przepływu z wierzchołka 0 do kazdego innego
    for t in range(1,n):
        print(t,maxFlowUndirected(G,s,t))
        k = min(k,maxFlowUndirected(G,s,t))

    return k

G = [
        [0,1,0,1,1],
        [1,0,1,0,0],
        [0,1,0,1,0],
        [1,0,1,0,1],
        [1,0,0,1,0],
]
print(edgeConnectivity(G))