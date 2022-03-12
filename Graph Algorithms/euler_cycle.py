# Algorytm, który szuka w grafie cyklu Eulera (to taki cykl, który przechodzi przez każdą krawędź tylko raz).
# Warunki na cykl Eulera:
# 1) graf musi być spójny
# 2) każdy wierzchołek musi być stopnia parzystego minimum 2 (nie może posiadać wierzchołków izolowanych)

# Implementacja dla reprezentacji macierzowej, 1 - krawędź, 0 -brak krawędzi.

# sprawdza czy kazdy wiercholek jest parzysty oraz czy nie ma wierzcholkow izolowanych
def isDegreeEven(G):
    for i in range(len(G)):
        cnt = 0
        for j in range(len(G)):
            if G[i][j] == 1:
                cnt += 1
        if cnt % 2 != 0 or cnt == 0:
            return False
    return True


def cycle(G):
    n = len(G)
    order = []
    visited = [False] * n

    def DFSvisit(u):
        visited[u] = True
        for v in range(n):
            if G[u][v] == 1:
                # odznaczam krawedzie odwiedzone
                G[u][v] = G[v][u] = 2
                DFSvisit(v)

        order.append(u)

    DFSvisit(0)

    # sprawdza czy graf jest spójny
    for i in range(n):
        if not visited[i]:
            return False

    return order


def eulerCycle(G):
    if isDegreeEven(G):
        return cycle(G)
    return False
