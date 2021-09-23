#ścieżka o najmniejszym iloczynie krawędzi z s do e
#wagi krawędzi nalezą do liczb naturalnych dodatkich bez zera

#wykonujemy zwykły algorytm dijikstry
#z taką różnicą że bedzie brac wartosci logarytmow krawedzi
#dzieki temu minimalizujac ich sume realnie zminimalizujemy iloczyn
#bo: log(x) + log(y) = log(xy)
#korzystam z log by nie miec DUŻYCH WARTOŚCI (iloczyn bardzo szybko rośnie)
#wiec normalnie mozemy dodawac krawędzie(dodajemy logarytmy krawędzi)
#ale bedzie tak na prawde nam sie tworzyła ściezka o min iloczynie
#a nas interesuje odtworzenie ścieżki a parenci będą poprawni
#O(ElogV)

from queue import PriorityQueue
from math import log10

def Dijikstra(G,s,e):
    n = len(G)
    inf = float("inf")

    parent = [None] * n
    visited = [False] * n
    dist = [inf] * n
    dist[s] = 0

    q = PriorityQueue()

    for i in range(n):
        if i != s:
            q.put((inf,i))
        else:
            q.put((0,i))

    while not q.empty():
        weight_u, u = q.get()

        if not visited[u]:
            visited[u] = True

            for i in range(len(G[u])):
                weight_v, v = G[u][i]
                if dist[u] < inf and dist[v] > dist[u] + log10(weight_v):
                    dist[v] = dist[u] + log10(weight_v)
                    parent[v] = u
                    q.put((dist[v],v))

    path = []
    last = e
    while last != s:
        path.append(last)
        last = parent[last]
    path.append(s)

    return path[::-1]


#waga,wierzcholek
G = [
    [(5,3),(3,4),(2,1)],
    [(4,2)],
    [(8,3),(1,4),(4,1)],
    [(8,2),(5,0),(2,4)],
    [(1,2),(3,0),(2,3)],
]
print(Dijikstra(G,0,2))
#najkrotsza 0,4,2
