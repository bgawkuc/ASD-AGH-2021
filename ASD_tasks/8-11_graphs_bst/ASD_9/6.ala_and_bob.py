# Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to miasta a krawędzie to drogi łączące miasta.
# Dla każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba naturalna). Alicja i Bob prowadzą (na zmianę) 
# autobus z miasta x ∈ V do miasta y ∈ V , zamieniając się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę 
# oraz decyduje, kto prowadzi pierwszy. Proszę zapropnować algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby
# Alicja przejechała jak najmniej kilometrów.

#Dijkstra, w której zostają podwojone tablice dist,visited,parent.
#Indeksy 0-n-1 oznaczają, zę do i-tego wierzchołka jechała Ala.
#Indeksy n-2n-1 oznaczają, zę do i-tego wierzchołka jechał Bob.
#Do kolejki wrzucam informacje kto prowadził do danego wierzchołka.
#Jeśli przez daną krawędź prowadzi Bob to liczę jej wartosć jako 0- bo minimalizuje trasę Ali.

from queue import PriorityQueue

def dijkstra(G,s,t):
    n = len(G)
    inf = float("inf")
    q = PriorityQueue()
    
    #gdy prowadzi Ala to mam idx o wartosci 0 <-> n - 1
    #gdy prowadzi Bob to mam idx o wartosci n <-> 2n - 1
    visited = [False] * (2*n)
    parent = [None] * (2*n)
    dist = [inf] * (2*n)

    dist[s] = 0
    dist[n+s] = 0
    
    #odległość od s, wierzchołek, kto kierował do ostatniego wierzchołka
    q.put((0,s,'A'))
    q.put((0,s,'B'))

    while not q.empty():
        _, u, driver = q.get()
        
        #gdy do u wjezdza A
        if driver == 'A': 
            visited[u+0] = True
             for edge, v in G[u]:

             #do v będzie jechał B, więc krawędź liczę jako 0, bo minimalizuje jedynie trasę A
             if dist[v+n] > dist[u+0] + 0 and not visited[v+n]: 
                dist[v+n] = dist[u+0] + 0
                parent[v+n] = u + 0
                q.put((dist[v+n],v,'B'))
                
        #gdy do u wjezdza B
        elif driver == 'B': 
            visited[u+n] = True
            for edge,v in G[u]:
                
                #do v będzie jechała A, więc liczę normalnie krawędź
                if dist[v+0] > dist[u+n] + edge and not visited[v+0]: 
                    dist[v+0] = dist[u+n] + edge
                    parent[v+0] = u + n
                    q.put((dist[v+0],v,'A'))

    
    #szukam kierowcy,który wjeżdża do wierzchołka t przy mniejszym dystansie jaki pokonała Ala
    if dist[t+0] > dist[t+n]: 
        betterDist = dist[t+n]
        curr = t + n
    else:
        betterDist = dist[t+0] 
        curr = t + 0
    
    #odtwarzam ścieżkę
    path = []
    last =curr

    while curr is not None:
        path.append(curr%n)
        curr = parent[curr]
        if curr is not None:
            last = curr

    if last >= n: firstDriver = "Ala"
    else: firstDriver = "Bob"
    
    #zwraca: ilość km przejechanych przez Ale, trasę, kto prowadził jako pierwszy
    return betterDist, path[::-1], firstDriver 
