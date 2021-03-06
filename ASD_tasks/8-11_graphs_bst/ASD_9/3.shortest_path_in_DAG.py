# Jak znaleźć najkrótsze ścieżki z wierzchołka s do wszystkich
# innych w acyklicznym grafie skierowanym?

# Należy wierzchołki posortować topologicznie, a następnie przechodzić po takiej posortowanej tablicy
# i dla każdego wierzchołka oraz krawędzi z niego wychodzących sprawdzać warunek na relaksacje.

def topologicalSorting(G):
    n = len(G)
    visited = [False] * n
    result = []

    def DFSvisit(u):
        visited[u] = True

        for edge, v in G[u]:
            if not visited[v]:
                DFSvisit(v)

        result.append(u)

    for i in range(n):
        if not visited[i]:
            DFSvisit(i)

    return result[::-1]


def shortestPath(G, s, t):
    inf = float("inf")
    n = len(G)

    topSort = topologicalSorting(G)
    parent = [None] * n
    dist = [inf] * n
    dist[s] = 0

    start = False

    for u in topSort:
        if u == s or start:
            start = True

            for edge, v in G[u]:

                # relaksacja
                if dist[v] > dist[u] + edge:
                    dist[v] = dist[u] + edge
                    parent[v] = u

    path = []
    last = t
    while last != None:
        path.append(last)
        last = parent[last]

    return path[::-1]
