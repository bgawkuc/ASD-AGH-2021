# Proszę zaimplementować algorytm obliczający domknięcie przechodnie grafu reprezentowanego w postaci macierzowej
# (domknięcie przechodnie grafu G, to graf nad tym samym zbiorem wierzchołków, który dla każdych dwóch 
# wierzchołków u i v ma krawędź z u do v wtedy i tylko wtedy, gdy w G istnieje ścieżka z u do v.

# Tworzę nowy graf G1 rozmiaru tego samego co rozmiar grafu wejściowego G.
# Dla każdego wierzchołka u wywołuje BFS, a tablicę visited zapisuje jako G1[u] w nowym grafie.
# Złożoność: O(V^3)

from queue import Queue
def BFS(G, s):
    n = len(G)
    q = Queue()
    visited = [0] * n

    q.put(s)

    while not q.empty():
        u = q.get()

        for v in range(n):
            edge = G[u][v]

            if edge == 1 and not visited[v]:
                visited[v] = 1
                q.put(v)

    return visited


def transitiveClosure(G):
    n = len(G)
    G1 = [[] for _ in range(n)]

    for s in range(n):
        G1[s] = BFS(G,s)

    return G1