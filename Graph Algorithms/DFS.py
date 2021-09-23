#DFS-Depth-first search, preszukiwanie w głąb
#Implementacja dla list sąsiedztwa
#Złożoność: O(V+E)

def DFS(G,s):
    visited = [False] * len(G)

    def DFS_visit(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_visit(v)

    DFS_visit(s)
