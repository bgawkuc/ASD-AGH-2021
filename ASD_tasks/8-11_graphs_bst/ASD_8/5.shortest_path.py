#zmieniony algorytm BFS do znalezienia najkrotszej sciezki z s do e
#i wypisania jej
#implementacja przez listę linked_list
#zlozonoszc O(v+e)

#wywoluje BFS dla wierzcholka startowego
#trwa on dopoki queue nie bedzie puste(brak rozw)
#albo pole koncowe zostanie odwiedzone
#sasiadow wierzcholka startowego dodaje do kolejki
#za kazdym razem zapamiętuje rodzica wierzcholka by móc odtworzyc sciezke
#oraz za kkazdym razem licze odlgl danego wierzcholka od startowego
#po wyjsciu z BFSa na podstawie tablicy rodzicow odtwarzam rozwiazanie

from queue import Queue
from math import inf

def solution(G, s, e):
    n = len(G)
    parent = [-1] * n #rodzic wierzcholka o idx i
    dist = [inf] * n #odleglosc wierzcholka i do s (startowego)
    visited = [False] * n

    def BFS(G):
        q = Queue()
        visited[s] = True
        dist[s] = 0
        q.put(s)

        while not q.empty():
            u = q.get() #wyjmuje el z kolejki

            for v in G[u]: #patrze po sąsiadach

                if not visited[v]: #gdy nie był jeszcze odwiedzony
                    visited[v] = True
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.put(v) #wkladam sąsiada do kolejki

                    if v == e: #gdy okaze sie ze doszlam do koncowego to koncze BFSa
                        return True
        return False

    if BFS(G) == False: #jesli nie istnieje droga do wierzcholka e
        return False

    path = [] #rozwiazanie
    path.append(e)

    while parent[e] != -1: #odtwarzam sciezke od tyłu, tzn zaczynajac od wierzcholka e, patrzac na rodzicow wierzch
        path.append(parent[e])
        e = parent[e]

    return path[::-1], len(path)

G =[
     [1,3],
     [2,0],
     [1],
     [4,7,0],
     [3,7,6,5],
     [6,4],
     [7,4,5],
     [6,4,3]
     ]
print(solution(G,2,6))