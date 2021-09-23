#algorytm Kruskala do znalezienia MST
#krawędź lekka - ta o najmniejzzej wadze

#wybieram po kolei krawędzie o najmniejszej wadze
#gdy jakis wierzch byl juz odwiedzony
#to szuka po jego sasiadach najmniejszej wagi i taką krawędź wybieram
#tylko musimy sie pilnowac by na zadnym etapie
#nasze wybrane krawedzie nie stanowiły cyklu

#algorytm
#sortuje krawędzie po wagach
#tworze tablice sets i pustą MST
#dla kazdego wierzch tworze zbior 1-elementowy
#przeglądam krawędzie grafu w kolejności rosnących wag
#dla krawedzie biore jej wierzch u oraz v
#sprawdzam czy korzen ze zbiorow dla kazdego z tych wierzchołków jesr różny
#jesli tak tzn ze nie tworzą one cyklu
#wiec krawędź dodaje do MST
#a zbiory dla wierzchołków u oraz v łączę za pomocą findUnion
#zwraca MST - zbiór krawędzi z wagą każda

class Node:
    def __init__(self, idx):
        self.idx = idx
        self.parent = self #kazdy el jest własnym rodzicem
        self.rank = 0


#zwraca "korzeń zbioru"
def findSet(x):
    if x != x.parent: #gdy zbiór jest wiecej niz 1 elementowy
        x.parent = findSet(x.parent) #szukam "korzenia"
    return x.parent #gdy znalazłam korzeń(jego rodzicem jest on sam)


#łączy 2 zbiory w 1(ten mniejszy przypina do wiekszego który jest korzeniem)
def union(x,y):
    #szukam korzeni moich zbiorow
    x = findSet(x)
    y = findSet(y)

    if x.rank > y.rank: #gdy x jest wyzszym drzewem
        y.parent = x #to y przypinam do niego

    elif y.rank > x.rank:
        x.parent = y

    else: #gdy są równej wys to dowlnie przypinam
        x.parent = y #wybrałam sobie ze y jest korzeniem
        y.rank += 1 #i wtedy wysokosc y sie zwieksza


def Kruskal2(G):
    n = len(G)
    edges = []

    #spisuje wszystkie krawedzie i sortuje je rosnąco
    for u in range(len(G)):
        for i in range(len(G[u])):
            edge = G[u][i][0]
            v = G[u][i][1]

            if not (edge,u,v) in edges:
                edges.append((edge,u,v))

    edges.sort(key=lambda x: x[0])

    MST = []
    sets = [Node(i) for i in range(n)]

    #przechpdze po krawedziach i jesli wierzcholki sa w osobnych zbiorach
    #to krawedz miedzy ni,i dodaje do mst, a na wierzcholkach(ich zbioracch) wykonuje union
    for edge,u,v in edges:
        if findSet(sets[u]) != findSet(sets[v]):
            MST.append((edge,u,v))
            union(sets[u],sets[v])

    return MST

G = [
    [(7,1),(1,2),(1,3)],
    [(7,0),(6,2),(1,4)],
    [(1,0),(6,1),(7,3)],
    [(1,0),(7,2),(7,4)],
    [(1,1),(7,3)]
]
print(Kruskal2(G))