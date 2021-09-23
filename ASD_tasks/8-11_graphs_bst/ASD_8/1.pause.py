#operator telefonicznt pause chce zakonczyc dzialanie w Pl
#chce wyłączyć wszystkie stacje nadawcze ktore tworzą graf połączeń
#trzeba to robić pojedyńczo
#podczas całego procesu wszyscy abonameci będący w zasięgu dzialajacych stacji
#muszą mieć możliwość łączenia się(czyli graf na kazdym etapie musi pozostać spójny)
#podaj algorytm który zwróci kolejność wyłączania stacji tak by graf był cały czas spojny

#jest to równoznaczne z tym:
#mam graf spojny nieskierowany
#okresl kolejnosc odczepiania wierzch tak by na kazdym etapie zostal spojny

#wykonuje dfs
#i odlaczam wierzcholki zaczynajac od tych o najwieksyzm czasie wejscia

def DFS(G,s):
    time = 0
    visited = [False] * len(G)
    order = [0] * len(G) #czasy wejscia

    def DFS_visit(u):
        nonlocal time
        time += 1
        visited[u] = True
        order[u] = time

        for v in G[u]: #dla sąsiadów u
            if not visited[v]:#jesli nie byl on jeszcze odwiedzony
                DFS_visit(v)


    DFS_visit(s)
    res = []

    for i in range(len(order)): #tworze tablice z krotkami(wierzcholek,czas wejscia)
        res.append((i,order[i]))
    print(res)

    res.sort(key= lambda x: x[1], reverse=True) #sortuje malejaco po czasach wejscia
    print(res)

    for i in range(len(order)): #kolejnosc odcinania, odcinam od najwiekszych czasow wejscia
        print(res[i][0])

G = [
    [2],
    [2],
    [0,1,3,5],
    [2,4],
    [3],
    [6,7,2],
    [5],
    [5],
]

G1 = [
    [1],
    [3,2,0],
    [3,1],
    [5,1,2,4],
    [3],
    [7,3,6],
    [9,7,8,5],
    [6,5],
    [6],
    [6],
]
print(DFS(G1,0))