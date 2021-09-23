#sciezka hamiltona

#to taka sciezka ktora przechodzi po wszystkich wierzcholkach a krawedzie sie nie powtarzaja
#jest to prblem NP-trudny
#znajdz sciezke hamiltona w acyklicznym grafie skierowanym

#przechodze po grafie dfs-gdy dojde do ostateniego wierzcholka dodaje go do res(tablica wynikowa)
#gdy dfs sie cofa z jakiegos wierzcholka to dodaje go do res
#na biezaco sprawdzam czy pomiedzy 2 ostatnio dodanymi wierzcholkami jest krawędź
#gdyby jej nie było tzn ze nie posiada takiej sciezki
#gdy nie wyrzuci nam bledu to zwracam res w odwroconej kolejnosci(bo dodawlam od konca)

#sprawdza czy jest krawedz z wierzcholka u do v
def isEdge(G,u,v):
    for z in G[u]:
        if z == v:
            return True
    return False

flag = True

def path(G):
    global flag
    res = []
    visited = [False] * (len(G))


    def DFSvisit(u):
        global flag
        visited[u] = True

        for v in G[u]: #przeszukuje liste dzieci

            if not visited[v]: #jesli ten wiercholek nie byl odwiedzony
                DFSvisit(v)

        res.append(u) #po przetworzeniu wierzcholka dodaje go do wyniku

        #działa
        #bo dla grafu: 1
        #             / \
        #            2   3  strzałka od 1 do 2 i od 1 do 3 nie ma sciezki ham
        #wiec najpierw by mi dodal 2 potem 3 i sprawdzi ze nie ma miedzy nimi krawedzi wiec zwroci False
        if len(res) > 1: #sprawdzam czy od ostatniego do przedostaniego wierzcholka jest krawedz
            #bo dodawane jest na odwrot do res
            if not isEdge(G,res[len(res)-1],res[len(res) - 2]):
                flag = False #gdyby nie bylo to nie moze posiadac tej sciezki



    for u in range(len(G)):
        if not visited[u]:
            DFSvisit(u)
            if not flag: #gdy flaga jest False tzn ze brakowalo krawedzi wiec nie ma cyklu
                return False

    return True,res[::-1] #bo dodawałam od tylu a jest skierowany

#posiada
G = [
    [1],[3],[4],[2,4],[],
]

#brak
G1 = [
    [1],[3],[4],[4], [],
]
#brak
G2 = [
    [1,2],[],[],
]

#istnieje, zaczyna sie w wierzchołku 3
G3 = [
    [],[0],[1],[2],
]
print(path(G1))
