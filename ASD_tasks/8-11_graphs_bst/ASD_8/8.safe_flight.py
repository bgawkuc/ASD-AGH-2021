#lece samolotem
#chce sie dostac z wierzcholka x do y
#krawedzie oznaczaja szerokosc korytarza lotu
#moge przelecieć przez dany korytarz jesli jego wymiar rozni sie o co najwyzeej t
#sprawdz czy taki lot jest mozliwy by utrzymac te zasady

#wyszukuje wszystkich sasiadow mojego wierzcholka startowego
#przeszukuje sasiadow po kolei
#w pętli tworzę wszystkie mozliwe przepustowosci:
#od krawedzi(start a sąsiad) - T do krawędzi + T
#i w pętli sprawdzam wszystkie mozliwe przepustowosci
#uruchamiam dfs dla wierzcholka x
#i sprawdzam czy byłam w stanie dotrzeć do wierzcholka y
#jesli ktoras z nich pozwoli mi wykonac lot to zwracam True
#jesli nie to zwracam False

#inny sposob - od Falisza
#robie sorta po pułapach
#i biore najmniejsza wartosc ustawiam to jako p
#mam okno jako pułap p + 2t
#sprawdzam czy start oraz end sa w tym p+2k
#jesli sa to robie DFS ktory sprawdza czy da sie z start dotrzec do end
#jesli sie da to koncze
#a jak nie to przesuwam okno dalej
#czyli biore kolejną wartosć pułapu(drugą najmniejszą)



def neighbour(G,s): #wypisuje mi sąsiadów wierzchołka
    neigh = []
    for i in range(len(G)):
        if G[s][i] != 0:
            neigh.append(i)
    return neigh


#x-start,y-koniec,P-wybrana przepustowość,T-granica o jaką moge przekroczyc przepusowosc
def DFS(G,x,y,p,t):

    def DFSvisit(u):
        visited[u] = True

        for v in neighbour(G,u):
            if abs(G[u][v] - p) <= t:
                if not visited[v]:
                    DFSvisit(v)

    visited = [False] * len(G)

    DFSvisit(x) #wywoluje dfs dla wierzcholka startowego
    return visited[y] #sprawdzam czy udało mi sie z niego dotrzec do wierzcholka y


def plane(G,x,y,t):
    for v in neighbour(G,x): #szukam sasiadow wierzch x(startowy)
        p = G[x][v] #wybieram sobie jedną z wartosci krawędzi sąsiadów

        for i in range(p-t,p+t+1): #przepustowosc ustawiam od sasiada - t, sasaiada + t

            if DFS(G,x,y,i,t): #sprawdzam czy jest to mozliwe dla wybranej przepustowosci
                return True

    return False #gdy DFS nogdy nie zwrocil prawdy tzn nie istnieje taka sciezka


G = [[0]*6 for i in range (6)]
G[0][4] = 19
G[4][0] = 19
G[0][3] = 26
G[3][0] = 26
G[1][4] = 22
G[4][1] = 22
G[1][2] = 18
G[2][1] = 18
G[2][3] = 23
G[3][2] = 23
G[5][2] = 25
G[2][5] = 25
G[4][5] = 21
G[5][4] = 21
#aby przeleciec z 0 do 1 musze leciec przez krawedz: 22 i 19
#średnia przepustowosc będzie 21 czyli granica 2->[21-2,21+2] bedzie spelniona
print(plane(G,0,1,2))