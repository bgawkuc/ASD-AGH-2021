#oblicz najwiekszy przepływ ale w grafie nieskierowanym

#algorytm forda-fulkersona działa dla grafów skierowanych
#w których między dowolną parą wierzchołków moze byc max 1 krawędź
#wiec trzeba stworzyc graf skierowany oparty na tym nieskierowanym
#tzn gdy miedzy wierzchołkami u,v w nieskierowanym znajduje sie krawedz to:
#dodaje krawędź skierowaną z u do v w nowym grafie
#oraz dodaje nowy wierzchołek k i dodaje 2 krawędzie skierowane z v do k i z k do u
#-> kazda krawędź jest o takiej samej wartoscu jak w grafie wejsciowym
#graf trzeba powiekszyc o tyle wiezchołków co ma krawędzi

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


def maxFlowUndirected(G,s,e):
    cntEdges = 0
    n = len(G)

    #zliczam ilosc krawedzi
    for i in range(n):
        for j in range(n):
            if i < j and G[i][j] != 0: #i < j warunek by krawędzie się nie powtarzały
                cntEdges += 1

    m = n + cntEdges #rozmiar nowego grafu to rozmiar starego + liczba krawędzi

    G1 = [[0] * m for _ in range(m)]

    newVertex = n #idx nowego wierzchołka

    #przechodze po starym grafie
    for u in range(n):
        for v in range(n):
            if u < v and G[u][v] != 0: #przechodze bez powtorzonych krawedzi
                G1[u][v] = G[u][v] #krawedz u -> v
                G1[v][newVertex] = G1[newVertex][u] = G[u][v] #krawędzie v -> newVertex, newVertex -> u
                newVertex += 1

    return fordFlukerson(G1,s,e)

G = [[0] * 5 for _ in range(5)]
G[0][1] = 8
G[1][0] = 8
G[0][4] = 6
G[4][0] = 6
G[1][2] = 3
G[2][1] = 3
G[1][3] = 9
G[3][1] = 9
G[2][3] = 5
G[3][2] = 5
G[2][4] = 7
G[4][2] = 7
G[3][4] = 2
G[4][3] = 2

print(maxFlowUndirected(G,0,4))
