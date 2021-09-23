#mam auto które porusza sie po grafie
#auto spala 1litr paliwa na 1 km
#mam podaną pojdemnosc baku c
#kazda krawędź ma jakąś wagę - długosc drogi(km)
#w kazdym wierzcholku mam stacje beznynową z cena pi za litr paliwa
#okresl najmniejsza kwotę za jaką jestem w stanie dojechac z miasta s do miasta e
#kiedy w wierzcholkach moge tankowac dowolną ilość paliwa

#musze stworzyc nowy graf
#który bedzie miał c * |V| wierzchołków więcej niż startowy
#dla kazdego wierzcholka vi tworze jego (c+1) wersji
#kazda jego wersja odpowiada il l w baku jaką mam stojąc w wierzchołku vi
#tzn bede miec vi - 0l, vi - 1l, vi - 2l, ..., vi - cl
#rowniez bede miec u1 - 0l, ui - 1l, ui - 2l, ui - cl
#w wejciowym grafie miedzy wierzcholkiem u a v znajdowala sie droga dlg x
#to teraz obliczam koszt drogi z kazdego do kazdego, są 2 opcje
#tzn:
#1) w wierzcholku vi nie tankuje paliwa wiec koszt krawedzi bedzie 0
#i krawedz przebiega z vi do ui o wartosci(vi il litrow - dlg drogi x)
#2) w wierccholku vi tankuje od 1 do (c- vi litrow) litrow
#wiec mam wtedy krawedz od vi do ui o wartosci(vi+il zatankowanych litrow - dlg drogi x)
#taka krawędź miałaby wartosc il zatankowanych litrow * cena paliwa w v
#powtarzam taką procedurę dla kazdego wierzcholka
#na koncu wykonuje dijkstre dla nowego grafu i mam od razu wynik
#macierz wejsciowa reprezentowana jako listy adjacencji

#2 SPOSÓB
#nie trzeba rozmnazac grafu
#mozna rozmnozyc tablice cost, parent, visited
#do kolejki wrzucam (0,s,d); d-pełny bak
#i potem sprawdzac do jakiego wierzcholka sie dotarlo -> v
#nr oryginalny wierzchołka + ilosc paliwa jaka została po dotarciu do v to idx w tablicach ktory bede sprawdzac
#i tak robie dopoki kolejka nie bedzie pusta
#wchodze z wierzcholka u do v, i teraz pytanie ile chce zatankowac w nim
#rozwazam tankowanie od 0-pelnego baku i odpowiednie wierzcholki wrzucam do kolejki
#a potem szukam minimum po wszystkich cost[t+paliwo] 0 <= paliwo <= d

#2 SPOSÓB
from queue import PriorityQueue

#p - ceny paliwa w wierzcholkach
#s,e - start, koniec
#c - pojemnosc baku
def tank(G, c, s, e, p):
    n = len(G)
    inf = float('inf')
    visited = [False] * (n * (c + 1))
    # koszt dostania sie do i-tego wierzcholka gdy w momencie wjazdu mam tam x(x<=c) paliwa
    cost = [inf] * (n * (c + 1))
    parent = [None] * (n * (c + 1))

    q = PriorityQueue()
    # dojazd do wierzcholka s majac c paliwa w baku wynosi 0 zl
    cost[s + c * n] = 0
    # koszt,-ilosc paliwa jaka jest w momencie wjazdu,wierzcholek
    q.put((0, -c, s + c * n))

    while not q.empty():
        _, currGas, u = q.get()
        # bo wkładam z minusem
        currGas = abs(currGas)

        if not visited[u]:
            visited[u] = True
            # przeglądam sąsiadów
            for edge, v in G[u % n]:
                # jesli da sie przejechac tę drogą
                if edge <= c:
                    # ile litrow tankuje w u
                    for tank1 in range(c+1):
                        # jesli po zatankowaniu nie przekrocze pojemnosci baku
                        # i starczy mi paliwa by przejechac edge
                        if currGas + tank1 <= c and currGas + tank1 >= edge:
                            # do v wjade majac currGas+tank1-edge paliwa
                            if cost[v + n * (currGas + tank1 - edge)] > cost[u] + tank1 * p[u % n] and \
                                    not visited[v + n * (currGas + tank1 - edge)]:
                                cost[v + n * (currGas + tank1 - edge)] = cost[u] + tank1 * p[u % n]
                                parent[v + n * (currGas + tank1 - edge)] = u
                                q.put((cost[v + n * (currGas + tank1 - edge)], -(currGas + tank1 - edge),
                                       v + n * (currGas + tank1 - edge)))

    path = []
    curr = e
    while curr is not None:
        # wierzcholek,z iloma litrami wjechał do tego wierzchołka
        path.append((curr % n, (curr - (curr % n)) // n))
        curr = parent[curr]

    # koszt wynosi
    return cost[e], path[::-1]


G1 = [
    [(6, 1)],
    [(6, 0), (2, 2), (2, 3)],
    [(2, 1), (1, 3), (7, 4)],
    [(2, 1), (1, 2), (5, 4)],
    [(7, 2), (5, 3)],
]
p1 = [3, 1, 2, 5, 1]
print(tank(G1, 10, 0, 4, p1))