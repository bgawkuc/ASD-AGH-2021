#mam graf ktory reprezentuje miasta i odleglosc od nich
#mam 2 kierowcow - Alicje i Boba
#ustal kto ma 1 prowadzic tak by A przejechała jak najmniej km
#wyznacz dlg tej trasy

#czyli mam 2 przypadki
#1)1 krawędź jedzie A
#2)1 krawędź jedzie B


#liczę to dijkstrą z tą różnicą ze tablice parent, visited, i dist tworze 2-krotnie wieksze
#jak mam idx od 0 do n - 1 to idx wierzchołka gdy prowadzi A do niego
#jak mam idx od n do 2n - 1 to idx wierzchołka gdy prowadzi B do niego
#np jak mam 4 wierzchołki to wierzchołkowi 1 odpowiada: 1(A do niego dojezdza) 5(1+4->B do niego dojezdza)
#do kolejki wrzucam wierzcholki tylko 0 <-> n - 1 ale tez informacje kto do tego wierzchołka prowadził
#i jak do u jechała A to sprawdzam czy dist dojazdu do v przez Boba da sie poprawic krawędzią u-v(jedzie nią B)
#a jak do u jechał B to sprawdzam czy dist dojazdu do v przez Ale da sie poprawic krawedzia u-v(jedzie nia A)
#i na koncu szukam minimum po dist[t] i dist[t+n] i wiem kto wjechal do wierzchołka t i i na bazie tego odtwarzam sciezke

from queue import PriorityQueue

#gdy prowadzi Ala to mam idx o wartosci 0 <-> n - 1
#gdy prowadzi Bob to mam idx o wartosci n <-> 2n - 1

def dijikstra(G,s,t):
    n = len(G)
    inf = float("inf")
    q = PriorityQueue()

    visited = [False] * (2*n)
    parent = [None] * (2*n)
    dist = [inf] * (2*n)

    dist[s] = 0
    dist[n+s] = 0

    q.put((0,s,'A'))
    q.put((0,s,'B'))


    while not q.empty():
        _, u, driver = q.get()

        if driver == 'A': #gdy do u wjezdza A
            if not visited[u+0]: #to sprawdzam czy wierzcholek wjazdu Ali do u nie był jeszcze przetwarzany
                visited[u+0] = True

                for i in range(len(G[u])): #sprawdzam dzieci wychodzące z u
                    edge, v = G[u][i]

                    #sprawdzam czy jadąc przez krawedz z u do v da się poprawic dystans do v Boba
                    #skoro do u prowadziła ala to do v bedzie prowadził Bob
                    if dist[v+n] > dist[u+0] + 0 and not visited[v+n]: #krawędź gdzie prowadzi Bob licze jako 0
                        dist[v+n] = dist[u+0] + 0
                        parent[v+n] = u + 0
                        q.put((dist[v+n],v,'B'))

        elif driver == 'B': #gdy do u wjezdza B
            if not visited[u+n]: #to sprawdzam wierzchołek wjazdu przez Boba czy nie był przetwarzany
                visited[u+n] = True

                for i in range(len(G[u])):
                    edge, v = G[u][i]

                    #teraz probuje poprawic wjazd do v przez Ale, gdy krawedz u-v przejezdza Ala
                    #WAZNE TU JEST VISITED BY NIE BYŁO KWADRATU
                    if dist[v+0] > dist[u+n] + edge and not visited[v+0]: #licze krawedz Ali
                        dist[v+0] = dist[u+n] + edge
                        parent[v+0] = u + n
                        q.put((dist[v+0],v,'A'))


    if dist[t+0] > dist[t+n]: #gdy taniej jest gdy to t wjezdza Bob
        betterDist = dist[t+n]
        curr = t + n #idx ostatniego wierzchołka
    else:
        betterDist = dist[t+0] #gdy taniej jest gdy to t wjezdza Ala
        curr = t + 0

    path = []
    first = inf

    while parent[curr] is not None:
        if curr >= n:
            path.append(curr-n)
        else:
            path.append(curr)
        first, curr = curr, parent[curr]
    path.append(s)

    if first >= n:
        firstDriver = "Bob"
    else:
        firstDriver = "Ala"

    return betterDist,path[::-1],firstDriver #ile km przejezdza Ala, trasa, kto zaczyna



#(waga,wierzcholek)
G = [
    [(10,1),(1,2)],
    [(10,0),(4,3),(7,4)],
    [(1,0),(8,4)],
    [(4,1),(6,5)],
    [(8,2),(7,1),(5,5)],
    [(6,3),(5,4)],
]
print(dijikstra(G,0,5))
