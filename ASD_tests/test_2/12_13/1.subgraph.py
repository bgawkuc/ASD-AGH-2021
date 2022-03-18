# Niech G = (V, E) będzie pewnym grafem nieskierowanym a U ⊆ V pewnym podzbiorem jego
# wierzchołków. Grafem indukowanym G|U nazywamy graf powstały z G przez usunięcie
# wszystkich wierzchołków spoza U. Proszę podać i zaimplementować wielomianowy algorytm,
# który mając na wejściu graf G = (V, E) (reprezentacja przez listy sąsiedztwa) oraz liczbę
# naturalną k, znajduje maksymalny co do rozmiaru zbiór U ⊆ V taki, że wszystkie wierzchołki
# w G|U mają stopień większy lub równy k. Proszę oszacować czas działania algorytmu.

from queue import PriorityQueue

def sugraph(G,k):
    n = len(G)
    degrees = [0] * n
    removed = [False] * n
    q = PriorityQueue()

    #wierzcholki umieszczam w kolejce ze stopniem jako klucz
    for u in range(n):
        deg = len(G[u])
        degrees[u] = deg
        q.put((deg,u))

    #wyjmuje wierzcholek i jego stopien
    #wyjmuje od najmniejszych stopnii
    deg, u = q.get()

    while deg < k:
        removed[u] = True

        for v in G[u]:

            if not removed[v]:
                degrees[v] -= 1
                q.put((degrees[v],v))
        deg, u = q.get()

    res = n
    for i in range(n):
        if removed[i]:
            res -= 1

    return res, removed #rozmiar pogdrafu indukowanego,

G = [
    [1,3,5],
    [0,2,3,5],
    [1,4,5],
    [0,1,4,5],
    [2,3],
    [0,1,2,3],
]
print(sugraph(G,3))
