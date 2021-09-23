#przeszukiwanie w głąb grafu
#depth first search

#  b - e
# /    | \        h
#a     d  \      /
# \   /    f -- g
#   c  -- /
#idź poki możesz a jak sie nie da to sie cofaj
#O(V+E) dla linked_list adj

def DFS(G,s):
    visited = [False] * len(G)

    def DFS_visit(u):
        nonlocal G, visited

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_visit(v)

    DFS_visit(s)

