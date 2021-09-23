#szuka max przepływu tak samo jak ford fulkerson
#ale przy zlozonosci O(EV^2)- LEPIEJ!

#działa bez BFSa i bez modyfikacji grafu
#tworze nową macierz F - rozmiarów takich jak macierz wejsciowa
#mowi nam ona ile juz wykorzystałam z danej krawedzi oraz dodaje krawędzie do sieci residualnej(tylko z wart ujemnymi)
#dopoki bede znajdowac jakąś sciezke do t do tego czasu algorytm sie wykonuje
#do kolejki wrzucam wierzch s
#dopoki kolejka nie jest pusta
#wyjmuje el z kolejki, przeglądam dzieci
#jesli istnieje krawędź do dziecka oraz do dzieck nie ma jeszcze rodzica
#oraz dziecko nie jest wierzchołkiem startowym
#oraz wartosc F[el][dziecko] jest mniejsza od wartosci krawędzi G[el][dziecko]
#czyli krawedz el-dziecko jeszcze nie została zuzywa do zera
#to parent[dziecko] = el i wrzucam dziecko do kolejki
#gdy kolejka bedzie pusta
#to n bazie parentow odtwarzam sciezke z t do s i szukam min przepustowosci
#a potem do kadzej krawedzi jaka była na trasie z s do t dodaje wartosc przepustowsci w tych krawedzaich w F
#oraz krawedzie w sieci residuanej w F -przepustowosc
#wynikiem max przepływu bedzie suma F[s]


from queue import Queue

def edmondsKarp(G,s,t):
    n = len(G)
    parent = None

    F = [[0] * n for _ in range(n)]

    while parent is None or parent[t] is not None: #jesli jest to 1 ruch, a potem dopoki istnieje sciekza do t
        q = Queue()
        q.put(s)
        parent = [None] * n
        #szukam jakiejs sciezki z s do t
        while not q.empty():
            u = q.get()

            for v in range(n):
                edge = G[u][v]

                if edge > 0: #gdy istnieje krawędź
                    #gdy v nie ma jeszcze rodzica
                    #gdy v nie jest startowym wiezrcholkiem
                    #gdy krawedz u-v nie została jeszcze w pełni wykorzystana
                    if parent[v] is None and v != s and F[u][v] < edge:
                        parent[v] = u
                        q.put(v)

        #gdy znalazlam sciezke z s do t
        if parent[t] is not None:
            flow = float("inf") #przepustowosc przepływu

            #szuka przepustowosci przepływu na obecnej sciezce
            u = t
            while parent[u] is not None and u != s:
                flow = min(flow, G[parent[u]][u]-F[parent[u]][u])
                u = parent[u]

            #tworze siec residualną
            u = t
            while parent[u] is not None and u != s:
                F[parent[u]][u] += flow
                F[u][parent[u]] -= flow
                u = parent[u]

    return sum(F[s]) #suma wiersza s to max flow



G = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

G1 = [
    [0,1,2,0],
    [0,0,0,2],
    [0,3,0,1],
    [0,0,0,0],
]
print(edmondsKarp(G,0,5))

