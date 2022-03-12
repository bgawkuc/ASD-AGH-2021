# Przewodnik chce przewieźć grupę K turystów z miasta A do miasta B. Po drodze jest jednak wiele innych miast 
# i między różnymi miastami jeżdzą autobusy o różnej pojemności. Mamy daną listę trójek postaci (x, y, c), 
# gdzie x i y to miasta między którymi bezpośrednio jeździ autobus o pojemności c pasażerów.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić na grupki tak,
# żeby każda grupka mogła przebyć trasę bez rodzielania się. Proszę podać algorytm, który oblicza na ile
# (najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), źeby wszyscy
# dostali się z A do B.

from queue import PriorityQueue


def reversePrim(G, s):
    n = len(G)
    q = PriorityQueue()
    inf = float("inf")

    visited = [False] * n
    parent = [None] * n
    max_weight = [-inf] * n
    max_weight[s] = 0

    for i in range(n):
        if i != s:
            q.put((inf, i))
        else:
            q.put((0, i))

    while not q.empty():
        _, u = q.get()
        visited[u] = True

        for edge, v in G[u]:

            if not visited[v] and edge > max_weight[v]:
                max_weight[v] = edge
                parent[v] = u
                q.put((-max_weight[v], v))

    return parent


def tourGuide(bus, s, t):
    n = len(bus)
    maxi = bus[0][1]

    for i in range(1, n):
        maxi = max(maxi, bus[i][1])

    G = [[] for _ in range(maxi + 1)]

    for x, y, edge in bus:
        G[x].append((edge, y))
        G[y].append((edge, x))

    parent = reversePrim(G, 0)

    path = []
    last = t

    while last != None:
        path.append(last)
        last = parent[last]

    return path[::-1]
