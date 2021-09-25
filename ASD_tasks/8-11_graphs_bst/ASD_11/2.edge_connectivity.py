# Dany jest graf nieskierowany G = (V, E). Mówimy, że spójność krawędziowa G wynosi k jeśli usunięcie
# pewnych k krawędzi powoduje, że G jest niespójny, ale usunięcie dowolnych k − 1 krawędzi nie rozspójnia go. 
# Proszę podać algorytm, który oblicza spójność krawędziową danego grafu.

#Aby obliczyć spójność krawędziową w grafie G należy policzyć wartość maksymalnego przepływu 
#od wierzchołka np. 0 do każdego innego (różnego od 0). Wśród tych wartości szukam najmniejszej, która
#stanowi spójność krawędziową grafu.

from queue import Queue
def BFS(G,s,t,parent):
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

    return visited[t]

#szuka max przepływu w grafie skierowanym
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

#szuka max przepływu w grafie nieskierowanym
def maxFlowUndirected(G,s,t):
    n = len(G)
    cntEdges = 0

    for u in range(n):
        for v in range(n):
            if u < v and G[u][v] != 0:
                cntEdges += 1
    
    #rozmiar nowego grafu
    m = n + cntEdges 
    G1 = [[0] * m for _ in range(m)]
    newVertex = n 

    for u in range(n):
        for v in range(n):
            if u < v and G[u][v] != 0:
                G1[u][v] = G[u][v]
                G1[v][newVertex] = G1[newVertex][u] = G[u][v]
                newVertex += 1
                
    return fordFulkerson(G1,s,t)

#oblicza spójność krawędziową grafu G(reprezentacja macierzowa)
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
