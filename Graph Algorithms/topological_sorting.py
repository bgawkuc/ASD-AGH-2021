#DAG - directed acyclic graph
#dotyczy grafow skierowanych, acyklicznych
#sortowanie topologiczne dagu polega na ulozeniu wierzcholkow w takiej
#kolejnosci ze krawedzie wskazuja tylko z lewej na prawą

#to takie sortowanie wierzchołków
#w ktorym jesli istnieje krawedz od x do y to x znajdzie sie przed y
#zastosowania
#a ---> b zadanie b musi byc wykonane przed a

#algorytm:
#wykonac DFS
#po przetworzeniu danego wiezrcholka dopisujemy go na poczatek listy
#przetworzony czyli przeszlam z niego do wszystkich mozliwych wierzcholkow
#a na koncu zwracam taką listę tylko że odwróconą

def DFS(G):
    order = []
    visited = [False] * len(G)

    def DFSvisit(u):
        visited[u] = True
        for i in range(len(G[u])):
            v = G[u][i]
            if not visited[v]:
                DFSvisit(v)

        order.append(u)

    for u in range(len(G)):
        if not visited[u]:
            DFSvisit(u)

    return order[::-1]

G = [
    [1,2,4],
    [2,3],
    [],
    [5,6],
    [3],
    [],
    [],
]

G1 = [
    [1],
    [2,3],
    [0],
    [4],
    [5],
    [3],
]

print(DFS(G1))