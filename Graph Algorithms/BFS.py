#przeszukiwanie w szerz grafu metodą BFS
#d first search

#mamy graf o wiercholkach a-h
#mamy fale ktora odgradza kolejne wierzcholki
#  b - e
# /    | \        h
#a     d  \      /
# \   /    f -- g
#   c  -- /

#1 fala odcina a
#2 fala odcina b c
#3 fala odcina d e f
#4 fala odcina g
#5 fala odcina h

#zlozonosc dla rep.listowej O(v+e)
#zlozonosc dla rep.macierzowej O(v^2)

from queue import Queue
#mozna dodac pole parent
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

