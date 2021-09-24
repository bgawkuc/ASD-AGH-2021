#mam N miast
#kazde posiada współrzedne (x,y)
#chcemy wybudowac siec autostrad tak aby z kazdego miasta dało sie dotzrec do kazdego
#i aby roznica miedzy zakonczeniem budowy najpozniejszym a najwczesniejszym była minimalna
#czas budowy autostrady z i do j to: sufit z sqrt((xi-xj)^2 + (yi-yj)^2)

#czyli wystarczy mi wybudowac n - 1 dróg aby połączyc n wierzchołków
#cztli szukam takiego mst w którym roznice miedzy wartosciami krawedzi sa mozliwie najmniejsze
#wykorzystam do tego find union
#majac zbior krawedzi posprtowany rosnąco
#oraz zbiór set dla każdego wierzchołka
#moge wybrac dana krawedz do mojej sciezki jesli rodzic dla wierzch u jest rozny od rodzica wierzch v
#gdzie u,v to wierzcholki przylagajace do tej krawedzi
#gdy wybiore juz n - 1 krawedzi to sprawdzam roznicy max - min i porwonuje ją z obecna min roznicą
#powtarzam tą pracedurę zaczynając od krawedzi o idx 0,1,...az do krawedzi takiej ze z nia jest tylko n - 1 krawedzi

from math import ceil,sqrt,inf
class Node:
    def __init__(self,idx):
        self.idx = idx
        self.parent = self
        self.rank = 0

def findSet(x):
    if x != x.parent: #jesli nie natrafiłam na korzeń
        x.parent = findSet(x.parent)
    return x.parent

def union(x,y):
    x, y = findSet(x), findSet(y)

    if x.rank > y.rank:
        y.parent = x
    elif y.rank > x.rank:
        x.parent = y
    else:
        x.rank += 1
        y.parent = x

def dist(xi,yi,xj,yj):
    return ceil(sqrt( (xi-xj) ** 2 + (yi-yj) ** 2 ))


def highway(G): #G-krotki z wspólrzednymi miast
    edges = []
    n =len(G)

    for i in range(n):
        for j in range(i+1,n):
            edges.append((i, j, dist(G[i][0],G[i][1],G[j][0],G[j][1]))) #nr miast, nr miasta, dlg budowy krawedzi miedzy nimi

    m = len(edges)
    edges.sort(key= lambda x: x[2]) #sortuje rosnąco
    minDif = inf #min roznica

    for i in range(m-n+1): #idx krawędzi od której zacyznam wybieranie krawędzi

        sets = [Node(i) for i in range(n)]
        mini, maxi = inf, -inf #min i max czas budowy na mojej sciezce
        lenPath = 0

        for j in range(i,m): #i-idx krawędzi od której zaczynam sprawdzanie
            if lenPath == n - 1: #gdy juz znalazlam sciezke o dlg n - 1
                minDif = min(minDif,maxi-mini)
                break

            city1, city2, edge = edges[j]

            if findSet(sets[city1]) != findSet(sets[city2]): #czy korzenie są rózne,(aby nie brac cykli), tylko mst
                mini = min(mini, edge)
                maxi = max(maxi, edge)
                union(sets[city1],sets[city2])
                lenPath += 1 #zwiekszam dlg sciezki

    return minDif

A =[(10,10),(15,25),(20,20),(30,40)]
print(highway(A))