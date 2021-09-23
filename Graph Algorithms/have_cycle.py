#Algorytm, który sprawdza czy graf posiada cykl.
#Implementacja dla reprezentacji macierzowej.
#Złożoność: O(V^2)

from queue import Queue

def BFS(G):
    n = len(G)
    queue = Queue()
    visited = [False] * n
    parent = [None] * n

    queue.put(0)
    visited[0] = True

    while not queue.empty():
        u = queue.get()
        for v in range(n):
            
            #0-brak krawędzi
            if G[u][v] != 0:
                
                #gdy mam odwiedzony wierzchołek v i u nie jest rodzicem v tzn, że trafiłam na cykl
                if visited[v]:
                    if u != parent[v]:
                        print("have cycle")
                        return

                else:
                    visited[v] = True
                    parent[v] = u
                    queue.put(v)
