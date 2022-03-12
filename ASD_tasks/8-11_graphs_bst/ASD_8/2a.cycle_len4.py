# Dany jest graf nieskierowany G zawierający n wierzchołków. Zaproponuj algorytm, który stwierdza
# czy w G istnieje cykl składający się z dokładnie 4 wierzchołków. Zakładamy, że graf reprezentowany jest przez macierz sasiedztwa A

def cycleOfLength4(G):
    n = len(G)
    res = [-1] * 4

    def DFSvisit(G, u, parent, cnt=3):
        nonlocal start
        res[cnt] = u

        if cnt >= 0:
            for v in range(n):
                if G[u][v] != 0:

                    if v != start and v != parent and cnt != 0:
                        DFSvisit(G, v, u, cnt - 1)

                    elif v == start and cnt == 0:
                        print(res)
                        exit(0)

    for u in range(n):
        start = u
        DFSvisit(G, u, u)
