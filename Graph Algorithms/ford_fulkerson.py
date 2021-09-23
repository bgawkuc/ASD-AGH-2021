#algorytm Forda-Fulkersona znajdujący maxymalny przeplyw grafu

#mam graf skierowany w ktorym kazda krawędź ma okreslony przeplyw
#musze okrelic takie sciezki z źródła do ujścia aby zachowana była zasada
#do kadego wierzchołka(poza s i e) tyle samo wpływa co wypływa
#zakładam ze w kazdej parze wierzchołków moze istniec tylko 1 sciezka skierowana

#polega na zwiekszaniu przepływu dopoki istnieje sciezka z s do e
#(dopoki nie zmniejsze krawędzi do 0)
#czyli dopoki jestesmy w stanie znalezc sciezke powiekszajacą to to robimy
#dla reprezentacji macierzowej

#odpalam BFS dopoki istnieje ścieżka z s do t
#w kazdej iteracji mam liste parentow
#na jej bazie odtwarzam ściezke od s do t i szukam w niej najmniejszej krawedzi
#jak ją znajde to jej wartosc dodaje do max przepływu
#oraz o jej wartość zmniejszam przepływ kazdej z odwiedzonych śćieżek na trasie
#powtarzam to dopoki będą istnieć jakiekolwiek ściezki z s do t
#(czyli nie wyzeruje mi tak krawędzi że sie nie będzie dało przejść)



#zlożoność O(EV^3)
from queue import Queue

def BFS(G,s,t,parent):
    n = len(G)
    visited = [False] * n

    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        u = q.get()

        for i in range(n):
            if G[u][i] != 0 and not visited[i]: #wartosc krawędzi musi być różna od 0 by istniała
                parent[i] = u
                visited[i] = True
                q.put(i)

    return visited[t] #sprawdza czy istnieje ściezka z s do t


def fordFulkerson(G,s,t):
    n = len(G)
    parent = [False] * n
    maxFlow = 0 #najwiekszy przepływ

    while BFS(G,s,t,parent): #jesli z s da sie dotrzec to t
        u = t
        mini = float("inf") #najmniejsza wartosc krawędzi na ścieżce z s do t

        #szukam najmniejszej krawędzi na trasie z s do t
        while u != s:
            if G[parent[u]][u] < mini:
                mini = G[parent[u]][u]
            u = parent[u]

        maxFlow += mini #taką najmniejszą krawędź dodaje do mojego max przepływu

        u = t

        #aktualizuje wartosci krawędzi zwykłych i tych powrotnych
        while u !=  s:
            G[parent[u]][u] -= mini #zmniejszm o wartosc tej krawędzi wszystkie z mojej sciezki
            G[u][parent[u]] += mini #tworze krawędzie powrotne, tworzy się sieć residualna
            u = parent[u]

    return maxFlow

G = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]
print(fordFulkerson(G,0,5))