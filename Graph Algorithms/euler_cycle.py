#szukam w grafie cyklu eulera
#cykl eulera-taka droga w grafie ktora przechodzi po kazdej krawedzi 1 raz
#aby cykl eulera istanial to graf musi byc, spojny i stopien kazdego w musi byc parzysty(rózny od 0!)
#gdy odwiedze jakąs krawedz wspisuje 2 zamiast 1

#algorytm
#wykonuje DFS usuwajac na biezaco kraw po ktorych wedrujemy
#zapisuje przy okazji odwiedzone wierzcholki w visited
#po przetworzeniu wierzcholka dodajemy go na poczatek listy wynikowej
#czyli odtwarzam sciezke od tylu i tak dopisuje do tablicy

#sprawdzam najpiew czy kazdy stopien wierzcholka jest parzystego stopnia lub czy nie jest izolowany
#gdyby nie był parzystego lub byl izolowany tzn ze nie posiada takiego cyklu
#potem wywoluje szukanie cyklu
#uzywam dfs gdy jakas krawedz bedzie odwiedzona to zmieniem jej wartosc na 2 by w nia nie wejsc ponownie

#sprawdza czy kazdy wiercholek jest parzysty oraz czy nie ma wierzcholkow izolowanych
def isDegreeEven(G):
    for i in range(len(G)):
        cnt = 0
        for j in range(len(G)):
            if G[i][j] == 1:
                cnt += 1
        if cnt % 2 != 0 or cnt == 0: #czyli jak nie ma stopnia parzystego lub jest wierzcholkiem izolowanym
            return False
    return True


def cycle(G):
    n = len(G)
    order = [] #kolejnosc odwiedzanych wierzcholkow
    visited = [False] * n

    def DFSvisit(u):
        visited[u] = True
        for v in range(n):
            if G[u][v] == 1:
                G[u][v] = G[v][u] = 2 #odznaczam krawedzie odwiedzone
                DFSvisit(v)

        order.append(u) #gdy rekurencja sie cofa to dodaje odwiedzony wiercholek

    DFSvisit(0)
    for i in range(n):
        if not visited[i]:
            return 'niespojny'

    return order


def eulerCycle(G):
    if isDegreeEven(G):
        return cycle(G)


G = [
    [0,0,1,1,0,0],
    [0,0,0,1,0,1],
    [1,0,0,1,0,0],
    [1,1,1,0,1,0],
    [0,0,0,1,0,1],
    [0,1,0,0,1,0],
]

G1 = [
    [0,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,1,0],
    [1,0,1,0,0],
    [1,1,0,0,0],
]

#niespojny
G2 = [
    [0,1,1,0,0,0],
    [1,0,1,0,0,0],
    [1,1,0,0,0,0],
    [0,0,0,0,1,1],
    [0,0,0,1,0,1],
    [0,0,0,1,1,0]
]
print(eulerCycle(G2))