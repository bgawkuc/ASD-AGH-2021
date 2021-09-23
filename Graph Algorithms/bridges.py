#dla grafow nieskierowanych/skierowanych
#most - krawędź w grafie która go rozspójnia
#tw - krawedz jest mostem gdy nie lezy na zadnym cyklu prostym w grafie
#krawedz wsteczna - krawedz wychodzaca do wierzcholka juz odwiedzonego
#czyli krawedz ktora nie nalezy do drzewa dfs bo wierzcholki ją tworzace sa juz odwiedzone
#zlozonosc taka jaka ma dfs O(v+e)

#algorytm
#wykonaj dfs dla kazdego wierzch zapisujac czas odwiedzenia
#zapisuje tez low dla kazdego wiezrcholka ktory na poczatku wyniesie tyle samo co czas odw
#w momencie gdy zaczynam sie cofac z jakiegos wierzch to spr low jego dzieci
#oraz low jego krawedzi wstecznych i biore minimum z tego ktore staje sie nowym low
#(wierzch juz odwiedzonych do ktorych on sie moze dostac)
#kiedy jakis rodzic dostal wartosc low nową i sie cofam to jego dzieci aktualizuje
#wtw gdy ich wartosci bylyby > od low rodzica i daje im low rodzica
#jego low i szukam najmn z tych wart
#d-czas odwiedzenia
#dla kazdego wierzch v licze low(v) = min(d(v), min(d(u)), min(low(w))
#min(d(u)) takie min gdzie mamy krawedz wsteczna z v do u
#low(w) w jest dzieckiem v w drzewie dfs- czyli sprawdzam wartosc low moich dzieci i szukam takiej najmniejszej
#mosty to krawedzie {v,p(v)} gdzie d(v) = low(v)
#p(v) parent v

#wywoluje DFS zapisujac czas odwiedzenia kazdego wierzcholka
#obliczam low(= min(d(u), d(v), min(low(w))) )
#u-wierzch do ktorego mam krawędź wsteczną,
#w to dziecko v
#mosty to krawedzie d(v) = low(v)

#wywoluje dfs, dane zapisuje w tablicach d(czas dotarcia) i l(wartosc d dla wierzcholka
#do ktorego uda sie nam wrocic-nie wracamy po glownej scizce ktora idzie dfs tylko tymi bocznymi)
#u-rodzic,v-dziecko
#jesli l[v] > d[u] tzn ze to jest most, po usunieciu u graf bylby niespojny


def DFS(G):
    time = 0
    n = len(G)
    bridges = []
    visited = [False] * n
    parents = [None] * n
    d = [0] * n #discovery time, czas dotarcia do wierzcholka
    l = [0] * n #najmniejsze mozliwe d wierzch do ktorego sie da wrocic idac po "dodatkowych" krawedziach

    def DFSvisit(u): #u - rodzic, v - dzieci
        nonlocal time
        time += 1
        d[u] = time
        l[u] = time
        visited[u] = True

        for v in G[u]: #v - dziecko

            if not visited[v]:
                parents[v] = u
                visited[v] = True
                DFSvisit(v)

                #zaczyna dzialac przy powrocie rekurencji, gdy sie cofam z dziecka do rodzica
                #zadziala gdy okaze sie ze dziecko ma mniejszą wartosc low niz rodzic
                #czyli ustala mi najlepsze czasy odwiedzenia (najkrotsza sciezka z startowego do u)
                l[u] = min(l[u],l[v]) #min po jego wart low oraz po wartosci low dziecka

                # if l[v] > d[u]: #gdy czas dodarcia do rodzica < najmniejszej mozliwiej drogi
                #     bridges.append([u,v])

            #gdy mam doczynienia z krawędzią wsteczną(czyli inna wracająco nie będąca rodzicem)
            #krawędzie wsteczne występują w cyklach
            elif visited[v] and parents[u] != v:
                #krawedz wsteczna do wierch v, ktory byl juz odwiedzony
                #sprawdzam czy wierzch z krawedzia wsteczna ma mniejsze d
                l[u] = min(l[u], d[v])


    for u in range(n):  #wywoluje dla wierzcholkow
        if not visited[u]:
            DFSvisit(u)

    for u in range(n):
        if d[u] == l[u] and parents[u] != None: #gdy wartosc d i low wierzch jest rowna oraz ma on rodzica
            bridges.append((parents[u],u)) #to istnieje most miedzy tym wierzch a rodzicem

    return bridges,d,l

G = [
    [1,6],
    [0,2],
    [1,3,6],
    [2,4,5],
    [3,5],
    [4,3],
    [0,2,7],
    [6]
]


print(DFS(G))