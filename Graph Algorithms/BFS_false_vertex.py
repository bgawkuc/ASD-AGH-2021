#BFS z wazonymi krawędziami
#gdy szukam nakrotszej sciezki z wierzchołka u do każdego innego

#BFS ze sztucznymi wierzchołkami
#reprezentacja przez listy adjacencji
#wkładam do kolejki wierzchołki w postaci
#(wierzchołek, ile zostało sztucznych wierzch, jego rodzic, waga krawedzi miedzy rodzicem a wierzch)
#na poczatku ilosc sztucznych wierz = waga krawedzi rodzic-dziecko - 1
#dopoki ilosc sztucznych wierzch nie wyniesie 0
#to przy sciaganiu tej krotki bede zmniejszac ilosc sztucznych wierzcholkow o 1
#gdy il. sztucznych wierzch bedzie 0
#oraz ten wierzch nie był odiwedzony
#to zaznaczam go jako odwiedzony i okreslam dist[wirzch] jako dist[rodzica] + dlg krawedzi miedzy wierzch a rodzicem
#i teraz wyszukuje wszystkie dzieci mojego wierzcholka i dodaje je do kolejki
#i dzięki temu mam długosc trasy od mojego wierzch startowego do kazdego innego

#OPŁACA SIĘ GO UŻYWAĆ GDY ZNAM WARTOŚCI KRAWEDZI-SĄ ONE OGARNICZONE BO WTEDY O(STAŁA*(V+E) CZYLI O(V+E)
#DLA NIEZNANYCH WAG O(MAX KRAWĘDŹ(V+E)) CZYLI POTENCJALNIE MOŻE TO BYĆ BARDZO DUŻE


from queue import Queue

#CZYTELNIEJSZA IMPLEMENTACJA
def BFS_false_vertex(G, u):
    n = len(G)
    q = Queue()
    visited = [False] * n
    dist = [None] * n

    # wierzcholek,ilosc sztucznych,rodzic,wartosc krawedzi
    q.put((u, 0, None, 0))
    visited[u] = True
    dist[u] = 0

    while not q.empty():
        u, cntFalse, parent, weight = q.get()
        if q.empty():
            q = Queue()

        # gdy nie przeszłam jeszcze wszystkich sztucznych
        if cntFalse > 0:
            q.put((u, cntFalse - 1, parent, weight))
        else:
            # gdy nie był jeszcze odwiedzony
            if not visited[u]:
                visited[u] = True

                if parent is None:
                    dist[u] = weight
                else:
                    dist[u] = weight + dist[parent]

            # wrzucam do kolejki wszystkie jego dzieci które nie były odwiedzone
            for v, edge in G[u]:
                if not visited[v]:
                    q.put((v, edge - 1, u, edge))

    return dist

#DRUGA IMPLEMENTACJA, PODOBNA
def BFS(G,u): #u wierzcholek z którego zaczynam
    q = Queue()
    n = len(G)
    visited = [False] * n
    dist = [False] * n #odleglosc od wierzch u do kazdego innego

    q.put((u,0,None,0)) #(wierzch,ilosc sztucznych wierzch,rodzic,waga kraw)
    visited[u] = True
    dist[u] = 0 #do samego siebie

    while not q.empty():
        v = q.get() #wierzcholek v z inf o jego rodzicu, il sztucznych wierzch i wadze krawedzi

        if q.empty():
            q = Queue()

        if v[1] != 0: #gdy zostaly mi jakieś sztuczne wierzchołki
            q.put((v[0],v[1]-1,v[2],v[3])) #to wkładam go dopoki dlg kraw nie wyniesie 0

        else: #gdy ściągnę wszystkie sztuczne wierzcholki

            if not visited[v[0]]: #gdy wierzcholek nie był jeszcze odwiedzany
                visited[v[0]] = True

                if v[2] is not None: #gdy ma rodzica
                    # to dotarcie do wierzch to dotarcie do jego rodzica + dlg krawedzi która ich łączy
                    dist[v[0]] = dist[v[2]] + v[3]
                else: #gdy nie ma rodzica
                    dist[v[0]] = v[3] #to dotarcie to jedynie dlg krawędzi

            for i in range(len(G[v[0]])): #dzieci wierzch v
                child = G[v[0]][i][0] #dziecko
                weight = G[v[0]][i][1] #waga dziecka

                if not visited[child]:
                    q.put((child,weight-1,v[0],weight)) #to wstawiam to dziecko do kolejki

    return dist #odleglosci do wszystkich wierzchołków z u

#(vertex,edge)
G = [
    [[1,2]],
    [[0,2],[2,3]],
    [[1,3],[3,5]],
    [[2,5],[4,10],[5,6]],
    [[3,10]],
    [[3,6],[6,6]],
    [[5,6],[7,1],[9,9]],
    [[6,1],[8,1]],
    [[7,1],[9,10]],
    [[6,9],[8,10]],
]
print(BFS(G,0))