# Proszę zaimplementować algorytm BFS tak, żeby znajdował najkrótsze ścieżki w grafie i następnie,
# żeby dało się wypisać najkrotszą ścieżkę z zadanego punktu startowego do wskazanego wierzchołka.

#Z użyciem BFSa przechodzę po grafie zapisując odległość do danego wierzchołka od startowego w tablicy dist.
#Na bazie tablicy rodziców odwzorowuje wygląd ścieżki.
#Implementacja przez listy sąsiedztwa.

from queue import Queue
from math import inf

def shortestPath(G, s, t):
    n = len(G)
    parent = [-1] * n 
    dist = [inf] * n 
    visited = [False] * n

    def BFS(G):
        q = Queue()
        visited[s] = True
        dist[s] = 0
        q.put(s)

        while not q.empty():
            u = q.get() 

            for v in G[u]:

                if not visited[v]: 
                    visited[v] = True
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.put(v)i
                    
                    #gdy istnieje ścieżka z s do t
                    if v == t: 
                        return True
        return False
    
    #jesli nie istnieje ściezka z s do t
    if not BFS(G): 
        return False

    path = [] 

    while t != -1: 
        path.append(t)
        t = parent[t]

    return path[::-1]
