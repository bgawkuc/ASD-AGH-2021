# BFS - breadth-first search, przeszukiwanie w szerz zaczynając od wierzchołka s.
# Reprezentacja grafu przez listy sąsiedztwa
# Złożoność: O(V+E)

from queue import Queue

def BFS(G, s):
    queue = Queue()
    visited = [False] * len(G)

    queue.put(s)
    visited[s] = True

    while not queue.empty():
        u = queue.get()
        
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                queue.put(v)
