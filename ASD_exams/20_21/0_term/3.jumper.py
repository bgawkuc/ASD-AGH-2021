# Dany jest ważony, nieskierowany graf G oraz dwumilowe buty - specjalny sposób poruszania się
# po grafie. Dwumilowe buty umożliwiają pokonywanie ścieżki złożonej z dwóch krawędzi grafu tak,
# jakby była ona pojedynczą krawędzią o wadze równej maksimum wag obu krawędzi ze ścieżki.
# Istnieje jednak ograniczenie - pomiędzy każdymi dwoma użyciami dwumilowych butów należy
# przejść w grafie co najmniej jedną krawędź w sposób zwyczajny. Macierz G zawiera wagi krawędzi
# w grafie, będące liczbami naturalnymi, wartość 0 oznacza brak krawędzi.
# Proszę opisać, zaimplementować i oszacować złożoność algorytmu znajdowania najkrótszej ścieżki
# w grafie z wykorzystaniem mechanizmu dwumilowych butów.
# Rozwiązanie należy zaimplementować w postaci funkcji:
# def jumper(G, s, w):
# ...
# która zwraca długość najkrótszej ścieżki w grafie G pomiędzy wierzchołkami s i w, zgodnie z zasadami używania dwumilowych butów.
# Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę przedstawić złożoność
# czasową oraz pamięciową użytego algorytmu.


def getMinVertex(visited, dist, n):
    v = -1
    d = float("inf")
    for u in range(n):
        if not visited[u] and dist[u] < d:
            v, d = u, dist[u]
    return v


def jumper(G, s, t):
    n = len(G)
    inf = float("inf")

    visited = [False] * (2 * n)
    dist = [inf] * (2 * n)
    dist[s] = dist[s + n] = 0

    longJump = [[inf] * (n ** 2) for _ in range(n ** 2)]

    for u in range(n):
        for v in range(n):
            for w in range(n):
                if u != v and v != w and u != w:
                    if G[u][w] > 0 and G[w][v] > 0:
                        longJump[u][v] = min(longJump[u][v], max(G[u][w], G[w][v]))

    for _ in range(2 * n):
        u = getMinVertex(visited, dist, 2 * n)
        if u == -1: break
        visited[u] = True

        for v in range(n):
            edge = G[u % n][v]

            if u < n and not visited[v + n] and dist[v + n] > dist[u] + longJump[u][v]:
                dist[v + n] = dist[u] + longJump[u][v]

            if edge > 0 and not visited[v] and dist[v] > dist[u] + edge:
                dist[v] = dist[u] + edge

    return min(dist[t], dist[t + n])


G = [
    [0, 1, 0, 0],
    [1, 0, 2, 0],
    [0, 2, 0, 3],
    [0, 0, 3, 0],
]
s, t = 0, 3
print(jumper(G, s, t))
