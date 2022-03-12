# W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć  wszystkie miasta siecią autostrad, 
# tak aby możliwe było dotarcie autostradą do każdego miasta. Ponieważ kontynent, na którym leży państwo jest
# płaski położenie każdego z miast opisują dwie liczby x, y, a odległość w linii prostej pomiędzy miastami
# liczona w kilometrach wyraża się wzorem len = sqrt((x1 − x2)^2 + (y1 − y2)^2). Z uwagi na oszczędności materiałów 
# autostrada łączy dwa miasta w linii prostej. Ponieważ zbliżają się wybory prezydenta, wszystkie autostrady zaczęto 
# budować równocześnie i jako cel postanowiono zminimalizować czas pomiędzy otwarciem pierwszej i ostatniej autostrady. 
# Czas budowy autostrady wyrażony w dniach wynosi ⌈len⌉ (sufit z długości autostrady wyrażonej w km). Proszę zaproponować
# algorytm wyznaczający minimalną liczbę dni dzielącą otwarcie pierwszej i ostatniej autostrady

# Tworzę tablice z wszystkimi możliwymi krawędziami między dowolną parą 2 wierzchołków, sortuje ją rosnąco.
# Korzystając z struktury find-union szukam drzewa rozmiaru n-1, w którym różnica pomiędzy najmniejszą, a największą
# krawędzią jest minimalna.

from math import ceil, sqrt, inf


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.parent = self
        self.rank = 0


def findSet(x):
    if x != x.parent:
        x.parent = findSet(x.parent)
    return x.parent


def union(x, y):
    x, y = findSet(x), findSet(y)

    if x.rank > y.rank:
        y.parent = x
    elif y.rank > x.rank:
        x.parent = y
    else:
        x.rank += 1
        y.parent = x


def dist(xi, yi, xj, yj):
    return ceil(sqrt((xi - xj) ** 2 + (yi - yj) ** 2))


# G-krotki z wspólrzednymi miast
def highway(G):
    edges = []
    n = len(G)

    for i in range(n):
        for j in range(i + 1, n):
            edges.append((i, j, dist(G[i][0], G[i][1], G[j][0], G[j][1])))

    m = len(edges)
    edges.sort(key=lambda x: x[2])
    minDif = inf

    for i in range(m - n + 1):

        sets = [Node(i) for i in range(n)]
        mini, maxi = inf, -inf
        size = 0

        for j in range(i, m):

            city1, city2, edge = edges[j]

            if findSet(sets[city1]) != findSet(sets[city2]):
                mini = min(mini, edge)
                maxi = max(maxi, edge)
                union(sets[city1], sets[city2])
                size += 1

            if size == n - 1:
                minDif = min(minDif, maxi - mini)
                break

    return minDif
