#Sprawdz czy zdany graf jest dwudzielny (rownowazne kolorowaniu grafu 2 kolorami).

#Wierzchołki w grafie koloruje na 2 kolory: 0 i 1.
#Aby był dwudzielny to nie może pojawić się sytuacja, w której wierzchołki należace do 1 krawędzi miałyby ten sam kolor.
#Implementacja przez listy sąsiedztwa.
#Złożoność: O(V+E).

from queue import Queue


def BFS(G):
    q = Queue()
    visited = [False] * len(G)
    color = [-1] * len(G)

    q.put(0)
    visited[0] = True
    color[0] = 1

    while not q.empty():
        u = q.get()

        for v in G[u]:

            if not visited[v]:
                visited[v] = True
                # koloruje na inny kolor niż ma u
                color[v] = 1 - color[u]
                q.put(v)

            if color[u] == color[v]:
                return False

    return True
