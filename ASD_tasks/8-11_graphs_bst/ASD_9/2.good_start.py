#mam graf skieorwany
#sprawdz czy istnieje w nim dobry początek
#to taki wierzcholek z ktorego da sie dotrzec do kazdego innego wierzcholka poprzez sciezke skierowana
#czyli nie musi wychodzi krawedzz  niego bezposrednio do kazdego innego
#wystarczy aby było posrednie dojscie do kazdego innego

#wywoluje dfs w ktorym zapisuje czas dotarcia do kazdego wierzcholka
#czasy dotarcia zaczynam od 1
#szukam wierzcholka dla ktorego czas dotarcia jest rowny rozmiarowi grafu
#bo jest wtedy szansa ze odiwedzilam wszystkie inne i na koncu trafilam do tegp
#sprawdzam czy da sie z niego dotzrec do kazdego wierzcholka
#sprawdzam to za pomocą DFS czy da mi on visited True dla kazdego wierzchołka
#jesli tak to jest on dobrym początkiem

def goodStart(G):
    n = len(G)
    finish = [-1] * n
    visited = [False] * n
    time = 0

    def dfsVisit(u):
        nonlocal time
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                dfsVisit(v)

        # czas pzretworzenia wierzcholka
        time += 1
        finish[u] = time

    # wywoluje dfs dla kazdego nieodwiedzonego wierzcholka
    for u in range(n):
        if not visited[u]:
            dfsVisit(u)

    for u in range(n):

        # jesli znajde wierzcholek ktorego czas przetworzenia wynosi tyle co rozmiar grafu
        # to moze on byc potencjalnie dobrym wierzcholkiem
        # wywołuje dla niego dfs i sprawdzam czy dotre do kazdego innego wierzcholka
        if finish[u] == n:
            visited = [False] * n
            dfsVisit(u)

            for i in range(n):
                if visited[i] == False:
                    return False
            return True, u

    return False


# 3 to dobry początek
G = [
    [],
    [0],
    [],
    [1, 2],
]
print(goodStart(G))

