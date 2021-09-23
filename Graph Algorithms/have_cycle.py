#napisz algorytm sprawdzajacy czy graf nieskierowany posiada cykl

#przwchodze BFSem graf zaczynajac w dowolnym wierzcholku
#dla kazdego wierzcholka zapisuje jego parenta
#gdy okaze sie ze przegladajac dzieci u trafie na dziecko v
#ktore bylo odwiedzone
#i okaze sie ze parent[v] == u tzn ze mam cykl

#sprawdza czy graf nie posiaada cyklu
def notHaveCycle(G):
    n = len(G)

    def isCycle(u,visited,parent):
        visited[u] = True

        for v in range(n):
            if G[u][v]:
                if not visited[v]:
                    parent[v] = u
                    if isCycle(v,visited,parent):
                        return True

                elif parent[u] != v:
                    return True
        return False

    for i in range(n):
        visited = [False] * n
        parent = [None] * n
        if isCycle(i,visited,parent):
            return False
    return True

from queue import Queue

def BFS(G, s):
    queue = Queue()
    visited = [False] * len(G)
    parent = [None] * len(G)

    queue.put(s)
    visited[s] = True

    while not queue.empty():
        u = queue.get()
        for v in range(len(G)):
            if G[u][v] == 1:

                if visited[v]:
                    if u == parent[v]:
                        continue
                    else:
                        print("have cycle",parent,u,v)
                        return

                else:
                    visited[v] = True
                    parent[v] = u
                    queue.put(v)

G = [
    [1], # 0 ma kraw z 1
    [2,4], # 1 ma kraw z 2 i 4
    [1,3], # 2 ma kraw z 1 i 3
    [2,4],
    [1,3],
]

G2 = [
    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],]
BFS(G2,0)
