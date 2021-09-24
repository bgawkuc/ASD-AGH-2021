#mam graf G = (V,E)
#mam znalezc sciezkie z s do e
#tak aby poruszac sie zawsze po malejacych krawedziach
#a suma wag krawedzi była mozliwie jak najmniejsza

#graf przedstawiony jako lista krawędzi (u,v,krawędź)

#sortuje po krawedziach malejaco
#a potem dla takiej posortowanej tablicy wykonuje relaksacje
#algorytm pominie wszystkie za duze krawedzie i zacznie dopiero zamieniac wartosci w dist
#gdy natrafi na wierzcholek startowy (dzieki temu zachowam warunek malejących krawędzi)
#a dalszy proces to relaksacja- znajdowanie najkrotszej sciezki
#jest to poprawne bo w śceizce krawędź wychodząca z wierzchołka startowego musi być najwieksza


from math import inf

def relax(u,v,edge,dist,parent): #krawedz z u do v
    if dist[v] > dist[u] + edge:
        dist[v] = dist[u] + edge
        parent[v] = u


def decreasing(edges,s,e,n): #n - rozmiar grafu
    edges.sort(key=lambda x: x[2], reverse=True) #sortuje po krawędziach malejąco
    dist = [inf] * n
    parent = [None] * n
    dist[s] = 0

    for u,v,edge in edges: #wierzcholek, wierzcholek, krawędź między nimi
        relax(u,v,edge,dist,parent)

    path = []

    #odtwarzam sciezke
    if dist[e] < inf:
        last = e
        while last is not None:
            path.append(last)
            last = parent[last]

    return path[::-1], dist[e]


edges = [[0,1,5],[1,2,3],[1,3,4],[1,4,6],[2,3,2],[3,4,1]]
edges1 = [[0,1,5],[1,0,5],[2,1,3],[1,2,3],[3,1,4],[1,3,4],[4,1,6],[1,4,6],[3,2,2],[2,3,2],[4,3,1],[3,4,1]]
edges2 = [[0,1,10],[1,0,10],[0,2,13],[2,0,13],[0,4,12],[4,0,12],[1,2,1],[2,1,1],[2,3,3],[3,2,3],[3,4,3],[4,3,3]]
graph = [[0, 1, 9],
         [1, 0, 9],
         [1, 2, 10],
         [1, 6, 8],
         [2, 1, 10],
         [2, 3, 4],
         [3, 2, 4],
         [3, 4, 5],
         [4, 3, 5],
         [4, 5, 6],
         [5, 4, 6],
         [5, 6, 7],
         [6, 1, 8],
         [6, 5, 7]]

print(decreasing(graph,0,2,7))

