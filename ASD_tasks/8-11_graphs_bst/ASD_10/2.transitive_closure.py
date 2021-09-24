#domknięcie przechodnie
#mam skierowany graf G w reprezentacji macierzowej
#z oznaczeniami krawędzi 1,0
#mam stworzyc Graf G1
#w grafie G1 istnieje krawedz z u do v wtw gdy w G istnieje sciezka skierowana z u do v
#czyli graf G1 to bedzię kopia G powiększona o sporo krawędzi
#zwróć G1

#wystarczy puscic BFS z kazdego wierzchołka
#i na jego podstawie stworzyc tablice wynikową
#wywołuje BFS dla kazdego wierzchołka
#i zapisuje jako i-ty wiersz tablice visited jaką on zwraca
#O(V^3)

from queue import Queue
def BFS(G, s):
    n = len(G)
    q = Queue()
    visited = [0] * n

    q.put(s)

    while not q.empty():
        u = q.get()

        for v in range(n):
            edge = G[u][v]

            if edge == 1 and not visited[v]:
                visited[v] = 1
                q.put(v)

    return visited


def transitiveClosure(G):
    n = len(G)
    G1 = [[] for _ in range(n)]

    for s in range(n):
        G1[s] = BFS(G,s)

    for i in range(n):
        print(G1[i])

#2 sposob
#wykorzystuje algorytm floyda warshalla
#tablice dist przerabiam na koncu
#jak dist < inf to wpisuje 1
#inaczej 0 -> brak krawędzi
#O(V^3)

def floydWarshall(G):
    n = len(G)
    dist = G[:] #tablica odleglosci
    p = [[None] * n for _ in range(n)] #tablica parentow

    for k in range(n): #wierzcholek "pomiedzy" u i v

        for u in range(n): #startowy

            for v in range(n): #koncowy

                if dist[u][v] == 0: #gdy nie mam krawedzi
                    dist[u][v] = float("inf") #to odlg ustalam na inf

                if dist[u][v] > dist[u][k] + dist[k][v]: #gdy poprzez wierzcholek k da sie taniej dostac z u do v
                    dist[u][v] = dist[u][k] + dist[k][v] #aktualizuje dystans
                    p[u][v] = k #aktualizuje rodzica

   #przerabiam tablice odlg na graf z 0(brak krawędzi) i 1(jest kraw)
    for i in range(n):
        for j in range(n):
            if dist[i][j] == float("inf"): #gdy pole ma wartosc i,j tzn ze nie dalo sie tarfic sciezka skierowaną z i do j
                dist[i][j] = 0
            else:
                dist[i][j] = 1

    for i in range(n):
        print(dist[i])

G = [
    [0,1,0],
    [0,0,1],
    [0,0,0],
]
G1 = [
    [0,1,0,0,1],
    [0,0,0,1,0],
    [0,0,0,0,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
]
transitiveClosure(G1)
print()
floydWarshall(G1)