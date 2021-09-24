# Przewodnik chce przewieźć grupę K turystów z miasta A do miasta B. Po drodze jest jednak wiele innych miast 
# i między różnymi miastami jeżdzą autobusy o różnej pojemności. Mamy daną listę trójek postaci (x, y, c), 
# gdzie x i y to miasta między którymi bezpośrednio jeździ autobus o pojemności c pasażerów.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich tursytów i musi ich podzielić na grupki tak,
# żeby każda grupka mogła przebyć trasę bez rodzielania się. Proszę podać algorytm, który oblicza na ile
# (najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), źeby wszyscy
# dostali się z A do B.

#Na bazie tablicy autobusów szukam największej wartości wierzchołka u i tworzę graf rozmiaru u + 1.
#Dodaje w grafie krawędzie ważone między każdymi 2 wierzchołkami między, którymi kursuje autubus.
#Dla takiego grafu wywołuje odwrócony algorytm Prima, który szuka drzewa rozpinającego o możliwie jak największych krawędziach.
#Najmniejsza krawędź w takim drzewie odpowiada pojemności każdego autobusu, a drzewo wyznacza dokładną trasę.

from queue import PriorityQueue

def reversePrim(G,s):
    n = len(G)
    q = PriorityQueue()
    inf = float("inf")

    visited = [False] * n
    parent = [None] * n
    #maksymalnie duza wartość krawędzi na trasie od s do i-tego wierzchołka
    max_weight = [-inf] * n

    max_weight[s] = 0

    for i in range(n):
        if i != s:
            q.put((inf,i))
        else:
            q.put((0,i))

    while not q.empty():
        _,u = q.get()
        visited[u] = True

        for edge,v in G[u]:

            if not visited[v] and edge > max_weight[v]:
                max_weight[v] = edge 
                parent[v] = u
                #wrzucam ujemną wartosc, by z kolejki wyciągać elementy o największych wartościach
                q.put((-max_weight[v],v)) 
    
    return parent


def tourGuide(bus,s,t):
    n = len(bus)
    maxi = bus[0][1] #max wartosc konca - rozmiar grafu

    #szukam max wartosci końca aby wiedziec jakiego rozmiaru stworzyc graf
    for i in range(1,n):
        maxi = max(maxi,bus[i][1])

    G = [[] for _ in range(maxi+1)]

    for x, y, edge in bus:
        G[x].append((edge, y))
        G[y].append((edge, x))

    parent = MST_Prim(G,0) #szukam paraentow dla drzewa o maksymalnie duzej minimalnej krawędzi

    #odtwarzanie ściezki
    path = []
    last = t

    while last != None:
        path.append(last)
        last = parent[last]

    return path[::-1]
