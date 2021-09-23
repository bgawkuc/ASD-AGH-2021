 #oblicza najkrotsze sciezki miedzy kazdą parą wierzchołkow
#dla grafów skierowanych
#algorytm który nawet dla krawedzi ujemnych da nam O(V^3)
#dopuszcza wagi ujemne ale nie moze byc ujemnego cyklu
#sprawdza sie szczegolnie dla grafów gestych
#dla grafow rzadkich mozna wywołać |V| razy Dijkstre lub Bellmana_Forda

#działa w sposob dynamiczny
#dla min sciezki z u do v szuka minimum po:
#1)obecnej sciezce z u do v
#2)sciezce z u do k + sciezce z k do v
#i zmienia obecna wartosc z u do v na tą mniejszą

#tworze sobie tablice 2d parentow i dist
#przechodze 3 pętlami
#1 to wierzcholek k przez ktory bede przechodzic
#2 to wierzcholek u - startowy
#3 to wierzcholek v koncowy
#dist[u][v] = min(dist[u][v]; dist[u][k] + dist[k][v])
#na końcu na bazie tablicy parentow odtwarzam rozwiązanie od tyłu

def floydWarshall(G):
    n = len(G)
    dist = G[:] #tablica odleglosci
    p = [[None] * n for _ in range(n)] #tablica parentow

    for k in range(n): #wierzcholek "pomiedzy" u i v

        for u in range(n): #startowy

            for v in range(n): #koncowy

                if dist[u][v] is None: #gdy nie mam krawedzi
                    dist[u][v] = float("inf") #to odlg ustalam na inf

                if dist[u][v] > dist[u][k] + dist[k][v]: #gdy poprzez wierzcholek k da sie taniej dostac z u do v
                    dist[u][v] = dist[u][k] + dist[k][v] #aktualizuje dystans
                    p[u][v] = k #aktualizuje rodzica /(p[k][v])

    return dist,p


#gdy chce odtworz yc sciezke
def getSolution(G,s,e):
    dist, p = floydWarshall(G)
    path = []
    curr = e
    #ściezke odtwarzam od tyłu
    while curr is not None:
        path.append(curr)
        curr = p[s][curr]

    path.append(s) #na końcu dodaje startowy wierzchołek

    return path[::-1], dist[s][e] #sciezka i odlgl z s do e

G = [
    [None, 10, None, 5, None],
    [None, None, 1, 2, None],
    [None, None, None, None, 4],
    [None, 3, 9, None, 2],
    [7, None, 6, None, None],
]


print(getSolution(G,0,2))