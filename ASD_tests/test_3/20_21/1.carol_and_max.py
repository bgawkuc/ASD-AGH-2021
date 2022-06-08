# Carol musi przewieźć pewne niebezpieczne substancje z laboratorium x do laboratorium y, podczas
# gdy Max musi zrobić to samo, ale w przeciwną stronę. Problem polega na tym, że jeśli substancje
# te znajdą się zbyt blisko siebie, to nastąpi reakcja w wyniku której absolutnie nic się nie stanie (ale
# szefowie Carol i Max nie chcą do tego dopuścić, by nie okazało się, że ich praca nie jest nikomu
# potrzebna). Zaproponuj, uzasadnij i zaimplementuj algorytm planujący jednocześnie trasy Carol
# i Maxa tak, by odległość między nimi zawsze wynosiła co najmniej d. Mapa połączeń dana jest
# jako graf nieskierowany, w którym każda krawędź ma dodatnią wagę (x i y to wierzchołki w tym
# grafie). W jednostce czasu Carol i Max pokonują dokładnie jedną krawędź. Jeśli trzeba, dowolne z
# nich może się w danym kroku zatrzymać (wówczas pozostaje w tym samym wierzchołku). Carol i
# Max nie mogą równocześnie poruszać się tą samą krawędzią (w przeciwnych kierunkach).
# Rozwiązanie należy zaimplementować w postaci funkcji:
# def keep_distance(M, x, y, d):
# ...
# która przyjmuje numery wierzchołków x oraz y, minimalną odległość d i graf reprezentowany przez
# kwadratową, symetryczną macierz sąsiedztwa M. Wartość M[i][j] == M[j][i] to długość krawędzi
# między wierzchołkami i oraz j, przy czym M[i][j] == 0 oznacza brak krawędzi między wierzchołkami.
# W macierzy nie ma wartości ujemnych. Funkcja powinna zwrócić listę krotek postaci:
# [(x, y), (u1, v1), (u2, v2), ..., (uk, vk), (y, x)]
# reprezentującą ścieżki Carol i Max. W powyższej liście element (ui, vi) oznacza, że Carol znajduje
# się w wierzchołku ui, zaś Max w wierzchołku vi. Można założyć, że rozwiązanie istnieje.

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


from queue import Queue


def BFS(G, s):
    n = len(G)
    visited = [False] * n
    parent = [None] * n

    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        u = q.get()

        for v in range(n):
            if G[u][v] == 1 and not visited[v]:
                visited[v] = True
                parent[v] = u
                q.put(v)

    return parent


def CarolAndMax(M, x, y, d):
    n = len(M)
    dist = floydWarshall(M)

    for i in range(n):
        print(dist[i])

    G = [[0] * (n ** 2) for _ in range(n ** 2)]

    vertex = [[-1, -1] for _ in range(n ** 2)]

    for i in range(n):
        for j in range(n):
            vertex[i * n + j][0] = i
            vertex[i * n + j][1] = j

    for i in range(n ** 2):
        for j in range(n ** 2):
            a, b = vertex[i]
            c, e = vertex[j]
            if i != j and a != b and c != e:
                if M[a][c] > 0 and M[b][e] > 0 and float("inf") > dist[c][e] >= d and (a, b) != (e, c):
                    G[i][j] = 1

    s = n * x + y
    parent = BFS(G, s)
    result = []

    t = y * n + x
    while t is not None:
        result.append(vertex[t])
        t = parent[t]

    return result[::-1]


M = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
]
x = 0
y = 3
d = 2

print(CarolAndMax(M, x, y, d))
