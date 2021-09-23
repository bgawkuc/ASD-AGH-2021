#mam szachownice n na n wypełnioną liczbami z zakresu 1-5
#oblicz koszt sciezki o minimalnym sumarycznym koszcie
#do pola n-1,n-1
#BŁĘDNA INTERPRETACJA - TRAKTUJE SZACHOWNICE JAK GRAF O N WIEZRCHOLKACH

#BFS ze sztucznymi wierzchołkami, BO WARTOSCI KRAWĘDZI SĄ OD 1 DO 5, CZYLI O(5*(V+E))
#tzn wkładam do kolejki kazdy wiezrcholek z iloscia sztucznych wierzch = waga kraw - 1
#dopoki ilosc sztucznych wiezrcholkow nie wyniesie 0 to przy sciagnieciu wierzch tylko zmniejszam ilosc stucznych
#gdy il sztucznych bedzie 0 a wierzch nie byl odwiedzony i ma rodzica
#to obliczam koszt dotarcia do niego
#jako koszt dotarcia do rodzica + krawedz miedzy nim a rodzicem
#i potem do kolejki dodaje wszystkie dzieci mojego wierzch które jeszcze nie były odwiedzone
#i na koncu sprawdzam wartosc tablicy dist[n-1] czyli koszt dotarcia do ostatniego wierzch
#tylko musze do niego dodac wartosc startowego pola by się zgadzalo

class Graph:
    def __init__(self,size):
        self.size = size
        self.arr = [[] for _ in range(size)]

    def addEdge(self,v,u,weight):
        self.arr[v].append((u,weight))
        self.arr[u].append((v,weight))


from queue import Queue

def kings_path(G,u,start): #u wierzcholek z którego zaczynam
    q = Queue()
    n = len(G)
    visited = [False] * n
    dist = [False] * n

    q.put((u,0,None,0)) #(wierzch,ilosc sztucznych wierzch,rodzic,waga kraw)
    visited[u] = True
    dist[u] = 0

    while not q.empty():
        u = q.get()
        if q.empty():
            q = Queue()

        if u[1] != 0: #gdy sciagnelam wierzcholek sztuczny
            q.put((u[0],u[1]-1,u[2],u[3])) #to wkładam go dopoki dlg kraw nie wyniesie 0

        else: #gdy nie mam juz sztucznych wierzchołków

            if not visited[u[0]]:
                visited[u[0]] = True

                if u[2] is not None: #gdy ma rodzica
                    # to dotarcie do wierzch to dotarcie do jego rodzica + dlg krawedzi która ich łączy
                    dist[u[0]] = dist[u[2]] + u[3]
                else:
                    dist[u[0]] = u[3]

            for v in range(n):
                weight = G[u[0]][v]

                if not visited[v]:
                    q.put((v,weight-1,u[0],weight)) #to wstawiam tego sąsiada do kolejki

    return dist[n-1] + start



A = [[1, 1, 2], #[0,1,2]
    [5, 6, 10], #[3,4,5]
    [4, 1, 1]]  #[6,7,8]

B = [[1, 1, 1, 5, 5],
    [5, 5, 1, 5, 5],
    [1, 1, 1, 5, 5],
    [1, 5, 5, 5, 5],
    [1, 1, 1, 1, 1]]

