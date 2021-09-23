#mam graf w którym wierzcholki przedstawiaja miasta
#mam przwodnika ktory chce przewieźć mozliwie jak najwieksza grupę osob
#grupa sie nie moze nigdy rozdzielic
#podaj tę trase
#na wejsciu dostaje graf z wierzcholkami oraz rozklad autobus
#autobus to krotka(wierz startowy, wierzch koncowy, max pojemnosc osob)

#tworze algorytm analogiczny do algorytmu prima
#musze wyznaczyc mozliwie najwiekszą wartosc pojemnosci
#czyli prim bedzie szukał drzewa o mozliwie jak najwiekszych wartosciach
#tzn najmniejsza wartosc w moim drzewie bedzie mozliwie jak najwieksza
#ale wsrod wszystkich pojemnosci uzytych atobusow musze wybrac najmniejsza
#(tak by zawsze cała grupa sie zmieściła)
#wiec do kolejki w mst będę wrzucac pojemnosci autobusow ale z minusem
#bo wtedy wyciaga mi od najwiekszych pojemnosci(bo to najmniejsze liczby przez minus)

#na podstawie tablicy autobusow tworze graf NIESKIEROWANY
#autobus-(x,y,pojemnosc)
#czyli dodaje krawedz z x do y o wadze pojemnosc
#ten graf przekazuje potem do prima
#na podstawie niego otrzymuje tablice parentow mojego drzewa
#jest to drzewo o mozliwie najwiekszych krawedziach
#i tak odtwarzam moją trase
#krawedz o min pojemnosci na mojej trasie to ilosc osob

from queue import PriorityQueue

def MST_Prim(G,s):
    n = len(G)
    q = PriorityQueue()
    inf = float("inf")

    visited = [False] * n
    parent = [None] * n
    max_weight = [-inf] * n #maksymalnie duza pojemnosc osob w autobusie na odinku od parenta do i-tego

    max_weight[s] = 0

    for i in range(n):
        if i != s:
            q.put((inf,i))
        else:
            q.put((0,i))

    while not q.empty():
        _,u = q.get()
        visited[u] = True

        for i in range(len(G[u])):
            edge,v = G[u][i]

            if not visited[v]:
                if edge != inf and max_weight[v] < edge: #jesli krawędź jest wieksza od tej obecnej dochadzacej do wierzcholka v
                    max_weight[v] = edge #to ją aktualizuje
                    parent[v] = u #aktualizuje rodzica
                    q.put((-max_weight[v],v)) #wrzucam ujemną wartosc by wyciągało mi od najwiekszych pojemnosci
    return parent


def tourGuide(bus,s,e):
    n = len(bus)
    maxi = bus[0][1] #max wartosc konca - rozmiar grafu

    #szukam max wartosci końca aby wiedziec jakiego rozmiaru stworzyc graf
    for i in range(1,n):
        if bus[i][1] > maxi:
            maxi = bus[i][1]

    G = [[] for _ in range(maxi+1)]

    for x, y, cap in bus:
        G[x].append((cap, y))
        G[y].append((cap, x))
    print(G)

    parent = MST_Prim(G,0) #szukam paraentow dla drzewa o maksymalnie duzej minimalnej krawędzi

    #odtwarzanie ściezki
    path = []
    last = e

    while parent[last] != None:
        path.append(last)
        last = parent[last]

    path.append(s)
    path = path[::-1] #moja sciezka od s do e

    i = 0
    bus.sort(key=lambda x : x[0]) #sortuje popoczatkach
    group = float("inf")

    #szukam najmniejszej pojemnosci na mojej trasie-wielkosc grupy
    #przechodze po autobusach kiedy trafie na taki co jedzie na trasie w path to sprawdzam czy jego pojemnosc < obecnej poj
    #jesli tak to aktulaizuje pojemnosc
    for x, y, cap in bus:
        if i == len(path) - 1:
            break
        if x == path[i] and y == path[i+1]:
            if cap < group:
                group = cap
                i += 1

    return path,group

#(u,v,edge)
bus = [(3,6,6),(5,6,6),(1,5,3),(2,3,5),(0,1,5),(0,2,4)]
print(tourGuide(bus,0,6))

