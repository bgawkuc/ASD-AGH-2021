# Dany jest ważony graf nieskierowany reprezentowany przez macierz T o rozmiarach n × n (dla
# każdych i, j zachodzi T[i][j] = T[j][i]; wartość T[i][j] > 0 oznacza, że istnieje krawędź między
# wierzchołkiem i a wierzchołkiem j z wagą T[i][j]). Dana jest także liczba rzeczywista d. Każdy
# wierzchołek w G ma jeden z kolorów: zielony lub niebieski. Zaproponuj algorytm, który wyznacza
# największą liczbę naturalną `, taką że w grafie istnieje ` par wierzchołków (p, q) ∈ V × V spełniających warunki:
# 1. q jest zielony, zaś p jest niebieski,
# 2. odległość między p i q (liczona jako suma wag krawędzi najkrótszej ścieżki) jest nie mniejsza
# niż d,
# 3. każdy wierzchołek występuje w co najwyżej jednej parze.
# Rozwiązanie należy zaimplementować w postaci funkcji:
# def BlueAndGreen(T, K, D):
# ...
# która przyjmuje:
# T: graf reprezentowany przez kwadratową macierz sąsiedztwa, gdzie wartość 0 oznacza brak
# krawędzi, a liczba większa od 0 przedstawia odległość pomiędzy wierzchołkami,
# K: listę przedstawiającą kolory wierzchołków,
# D: odległość o której mowa w warunku 2 opisu zadania.
# Funkcja powinna zwrócić liczbę ` omawianą w treści zadania.


import collections


def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = collections.deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for ind, val in enumerate(graph[u]):
            if (visited[ind] == False) and (val > 0):
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return visited[t]


def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow


def floydWarshall(G):
    n = len(G)
    dist = G[:]

    for k in range(n):
        for u in range(n):
            for v in range(n):

                if dist[u][v] == 0:
                    dist[u][v] = float("inf")

                if dist[u][v] > dist[u][k] + dist[k][v]:
                    dist[u][v] = dist[u][k] + dist[k][v]

    return dist


def blueAndGreen(G, K, d):
    n = len(G)
    dist = floydWarshall(G)
    new = [[0] * (n + 2) for _ in range(n + 2)]

    s = n
    t = n + 1

    for u in range(n):
        for v in range(n):
            if K[u] == 'B' and K[v] == 'G' and dist[u][v] >= d:
                new[u][v] = 1
                new[s][u] = 1
                new[v][t] = 1

    return edmonds_karp(new, s, t)


T = [
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
]
K = ['B', 'B', 'G', 'G', 'B']
D = 2
# wynik 2
print(blueAndGreen(T, K, D))
