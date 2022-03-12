# Pewien podróżnik chce przebyć trasę z punktu s do punktu t. Niestety jego samochód spala dokładnie jeden litr
# paliwa na jeden kilometr trasy. W baku mieści się dokładnie c litrów paliwa. Trasa jest reprezentowana jako graf,
# gdzie wierzchołki to miasta a krawędzie to łączące je drogi. Każda krawędź ma długość w kilometrach 
# (przedstawioną jako licza naturalna). W każdym wierzchołku jest stacja benzynowa, z daną ceną za litr paliwa.
# Proszę podać algorytm znajdujący trasę z punktu s do punktu t o najmniejszym koszcie. 

# Dijkstra, w której wszystkie użyte tablice rozmnażam c+1 razy.

from queue import PriorityQueue


# p - tablica z ceną za 1l paliwa w i-tym wierzchołku
# s,t - start, koniec
# c - pojemnosc baku
def tank(G, c, s, t, p):
    n = len(G)
    inf = float('inf')
    visited = [False] * (n * (c + 1))

    cost = [inf] * (n * (c + 1))
    parent = [None] * (n * (c + 1))

    q = PriorityQueue()

    # dojazd do wierzcholka s majac c paliwa w baku wynosi 0
    cost[s + c * n] = 0
    q.put((0, -c, s + c * n))

    while not q.empty():
        _, currGas, u = q.get()
        currGas = abs(currGas)
        visited[u] = True

        for edge, v in G[u % n]:
            if edge <= c:
                # ile litrow tankuje w u
                for tank1 in range(c + 1):

                    if currGas + tank1 <= c and currGas + tank1 >= edge:
                        leftGas = currGas + tank1 - edge

                        if cost[v + n * leftGas] > cost[u] + tank1 * p[u % n] and not visited[v + n * leftGas]:
                            cost[v + n * leftGas] = cost[u] + tank1 * p[u % n]
                            parent[v + n * leftGas] = u
                            q.put((cost[v + n * leftGas], -leftGas, v + n * leftGas))

    path = []
    curr = t
    while curr is not None:
        path.append(curr % n)
        curr = parent[curr]

    # zwraca min koszt tankowań, trasę
    return cost[t], path[::-1]