#algorytm bellmana forda
#obliczanie najkrótszych ścieżek w grafie skierowanym od wierzcholka s
#dopuszcza ujemne wagi krawędzi
#O(V*E)

#warunek: graf nie zawiera ujemnego cyklu - cykl w ktorym suma krawedzi jest ujemna
#gdyby tak było to algorytm w kółko by wędrował po tym cyklu znajdując co raz mniejsze sumy
#gdy taki cykl w nim sie zawiera to zwraca on false

#algorytm nie działa gdy zawiera on cykl o ujemnej sumie krawędzi

#algorytm
#tworze tablice parent i dist
#w pętli |V| - 1 razy (-> dlg najdluzszej mozliwej sciezki)
#wykonuje relaksacje dla kazdego wierzchołka i jego sasiadow
#czyli powtarzam ją V - 1 razy dla kazdej mozliwej krawędzi
#nastepnie weryfikuje czy nie zawiera on zadnego ujemnego cyklu
#czyli sprawdzam czy odgl do dziecka nie jest wieksza od sumy odgl do rodzica + krawedzi je łączących
#gdyby tak było tzn ze algorytm źle zadzialał(poprzez istenienie cyklu)
#bo nie znalazł najtańszej drogi do dziecka(przez istnienie ujemnegi cyklu)
#bo droga do dziecka jest drozsza niz droga do rodzica + łączaca ich krawędź
#wiec wtedy ma wyrzucic False


def bellmanFord(G, s):
    inf = float("inf")
    n = len(G)

    dist = [inf] * n
    parent = [None] * n
    dist[s] = 0

    for _ in range(n - 1):  #powtarzam procedure tyle razy co dlg najdluższej sciezki(|V|-1)

        for u in range(n):  # wierzcholek startowy sciezki

            for edge, v in G[u]:  # jego dzieci

                #relaksacja
                if dist[v] > dist[u] + edge and dist[u] != inf:
                    dist[v] = dist[u] + edge
                    parent[v] = u

    # weryfikacja
    for u in range(n):

        for edge,v in G[u]:

            #gdyby wynik zaczał sie poprawiac tzn ze trafiłam na ujemny cykl
            if dist[v] > dist[u] + edge and dist[u] != inf:
                return False

    return dist, parent

#(waga,wierzchołek)
#najmniejsza waga do 4 to -3: 0->1->3->4
G = [
    [(-2,4),(6,1)],
    [(1,3),(-7,2),(-1,4)],
    [(10,3)],
    [(-10,4)],
    [],
]

#zawiera ujemny cykl więc wyrzuci mi False
G1 = [
    [(-2,1)],
    [(1,2)],
    [(-1,0)],
]
print(bellmanFord(G,0))
