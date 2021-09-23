#algorytm do szukania najkrótszych ścieżek w grafie
#działa jak BFS z sztucznymi wierzchołkami
#z tą różnicą ze poza rozwazaniem sztucznych wierzchołków
#patrzy tez na te oryginalne
#NIE ZADZIAŁA DLA KRAWĘDZI O UJEMNYCH WAGACH

#działa tylko dla wag dodadatnich(0 tez jest dodatnie)

#algorytm
#s-startowy
#umiesc wszystkie wierzcholki w kolejce priorytetowej
#oz szacowaniem odlgl od S rownym s
#zmien odgls s na 0
#poki są wierzchołki w kolejce:
#wyjmij z kolejki wierzcholek u o minimalnym
#oszacowaniu odległości
#dla kazdej krawędzi {u,v} wykonaj relaksacje

#relaksacja:
#def relax(u,v):
#   if v.d > u.d + w({u,v}): $=#czyli mozna poprawic oszacowanie dojscia do u
#       v.d = u.d + w({u,v}) to poprawiam oszacowanie
#       v.parent = u

#O(ElogV) - dla linked_list wierzchołków


#opis
#reprezentacja dla listy sąsiadów
#kazdy wierzołek dodaje do kolejki z odlegloscią inf
#s - startowy
#tworze tablice dist - min odlg z wierzcholka s do i -tego
#i tablice parent - rodzic dla kazdego wierzcholka w najkrotszej trasie do niego
#z kolejki wyciągam wierzcholek u o najmniejszej wartości odległości
#sprawdzam jego sasiadow v
#jesli odleglosc dla jakiegos wierzcholka v do s jest wieksza niz
#niz odglegosc z s do u + krawedz {u,v}
#to aktualizuje odgl do v na suma odlg z s do u + {u,v}
#do kolejki wkładam wierzch v ze zmienioną, mniejszą odległością
#parentem v staje się teraz u
#ten proces sie powtarza dopoki kolejka nie zostanie pusta
#zwracam parentow i odleglosci
#wiec mam dostep do odlg od s do kazdego innego i moge odtworzyc trase od s do tego wierzch

from queue import PriorityQueue

#listy adj z pq
#O(ElogV)
def dijkstra(G,s):
    n = len(G)
    p = PriorityQueue()
    inf = float("inf")

    p.put((0,s))

    parents = [None] * n
    visited = [False] * n
    dist = [inf] * n #tablica najmniejszych odleglosci od wierzcholka s
    dist[s] = 0 #odlgl od s do s wynosi 0

    while not p.empty():
        _, u = p.get() #wyjmuje krotke (_ = odleglosc, u = wierzcholek) po najmniejszych odleglosciach
        visited[u] = True

        for i in range(len(G[u])): #szukam wsrod sasiadow wierzcholka u
            v, edge = G[u][i] #sąsiad u reprezantowany jako krotka (v-wierzch,w-waga),

            #relaksacja, czyli jak istnieje krótsza ścieżka
            # #jesli dlg trasy do wierzch v jest wieksza od trasy do wierzch u + wartosc krawedzi od u do v(w)
            if dist[v] > dist[u] + edge and not visited[v]:
                dist[v] = dist[u] + edge #aktualizuje dlg trasy do v
                p.put((dist[v],v)) #wsadzam wierzcholek v z zaktualizowaną dlg drogi
                parents[v] = u #aktualizuje rodzica v na u


    return dist, parents

#odtwarzanie ściezki z s do e
def findPath(G,s,e):
    dist, par = dijkstra(G,s)
    path = []
    path.append(e)
    el = par[e]

    while el is not None:
        path.append(el)
        el = par[el]
    return path[::-1]

#(vertex,edge)
G = [
    [[1,3],[4,10]],
    [[0,3],[2,6],[3,4]],
    [[1,6],[3,1]],
    [[1,4],[2,1],[4,2]],
    [[0,10],[3,2]],
]
print(dijkstra(G,0))


#dijikstra dla macierzowej repr bez PQ
#LEPSZA ZŁOŻONOŚĆ!
#O(V^2)

#szukam v o min dist ktory nie był jeszcze odwiedzony
def getMinVertex(visited, dist):
    v = -1
    d = float("inf")

    for i in range(len(dist)):
        if not visited[i] and dist[i] < d:
            d = dist[i]
            v = i
    return v


def dijikstra4(G,s):
    n = len(G)
    inf = float("inf")

    parent = [None] * n
    visited = [False] * n
    dist = [inf] * n
    dist[s] = 0

    for _ in range(n):
        #wierzcholek o min dist ktory nie byl jeszcze odwiedzony
        u = getMinVertex(visited,dist)
        visited[u] = True

        for v in range(n):
            edge = G[u][v]

            if edge != 0:
                if not visited[v] and dist[v] > dist[u] + edge:
                    dist[v] = dist[u] + edge
                    parent[v] = u

    return dist, parent

G = [
    [0,1,0,2,0,10],
    [1,0,2,0,5,0],
    [0,2,0,3,0,4],
    [2,0,3,0,8,0],
    [0,5,0,8,0,1],
    [10,0,4,0,1,0],
]
print(dijikstra4(G,0))