#szukam najkrotszej sciezki wazonej w grafie skierowanym acykliczym(drzewie)
#prowadzącej od s do e

#sortuje topologicznie wierzchołki
#i wykonuje dijkstre(dla posortowanej top tablicy - bezk kolejki) - LEPSZA ZŁOŻONOŚĆ
#wszystkie sciezki mają dlg inf poza tą z s do s która ma dlg 0
#zaczynam od s(tego co jest przed nim nie musze brac pod uwage)
#bo z definicji sortowania topologicznego wiem ze nie istnieje do nich
#zadna sciezka z s
#przegladam jego sąsiadów (v)
#i dla kazdego sąsiada odpalam algorytm relaksacji z (s do v)
#jako wynik otrzymam najktosze ściezki z s do kazdego osiągalnego wierzch


def topologicalSorting(G):
    n = len(G)
    visited = [False] * n
    result = []

    def DFSvisit(u):
        visited[u] = True

        for edge,v in G[u]:
            if not visited[v]:
                DFSvisit(v)

        result.append(u)

    for i in range(n):
        if not visited[i]:
            DFSvisit(i)

    return result[::-1]


def Dijkstra(G,s,e):
    inf = float("inf")
    n = len(G)

    topSort = topologicalSorting(G) #posortowane topologicznie krawedzie
    print(topSort)
    parent = [None] * n #rodzic kazdego wierzcholka
    dist = [inf] * n #odleglosc od s do kazdego innego
    dist[s] = 0

    start = False

    for u in topSort: #przegladam wierzcholki po posortowaniu topologicznym
        if u == s or start: #zaczynam dopiero od wierzch s
            start = True

            for edge,v in G[u]: #przegladam sąsiadów

                #CHYBA BRAKUJE POLA VISITED (albo nie bo nie ma pq)
                if dist[v] > dist[u] + edge: #relaksacja
                    dist[v] = dist[u] + edge
                    parent[v] = u

    #odtwarzanie ściezki
    path = []
    last = e
    while last != None:
        path.append(last)
        last = parent[last]


    return dist[e],path[::-1] #wartosc sciezki, sciezka



#(waga,dziecko)
G = [
    [(1,1),(1,4)],
    [(2,2),(10,3)],
    [(4,3)],
    [(2,4)],
    [(2,1)],
]
print(Dijkstra(G,0,3))