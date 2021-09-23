#mowimy ze wierzcholek t w grafie skierowanym jest uniwersalnym ujsciem jesli
#a) z kazdego innego wierzcholka v istnieje krawedz z v do t
#b) nie istnieje krawędź wychodząca z t
#podaj algorytm znajdujacy ujscie postaci macierzowej grafu

#warunek b->szukam takiego wiersza u ktory jest wypelniony tylko 0
#warunek a-> szukam takiej kolumny u wypelnionej samymi 1(poza M[u][u])
#gdy M[u][v] = 0 tzn ze krawedzi z u do v nie ma czyli v nie moze byc ujsciem
#gdy M[u][v] = 1 tzn ze z u do v jest krawedz to u nir moze byc ujsciem
#liniowo szukam kandydata na ujscie
#gdy M[u][v] == 0 to v++ ruch w prawo #potencjalnie dobry wiersz
#gdy M[u][v] == 1 to u++ ruch w dół #na pewno zly wiersz
#kiedy dojdziemy z v poza ostatnią kolumne tzn ze wierzcholek u jest kandydatem
#i tylko dla niego sprawdzamy czy u-ty wiersz sklada sie z samych zer
# a cata u-ta kolumna z samych 1(z wyjatkiem u-tego el)
#jesli wyjdziemy z v za ostatni wiersz tzn ze ujscia nie ma

def universal_sink(G):
    n = len(G)
    u, v = 0, 0

    while u < n and v < n: #poruszmam sie odpwiednio w prawo lub w dół

        if G[u][v] == 0:
            v += 1

        else:
            u += 1

    def is_sink(u): #sprawdza czy dany wierzcholek jest ujsciem
        for v in range(n):

            if G[u][v] == 1: #wiersz musi byc pelen 0
                return False

            if u != v and G[v][u] == 0: #kolumna musi byc pelna 1
                return False

        return True

    if u == n: #gdy wyjdę wierszem poza tablice
        return 'brak ujscia'

    else: #gdy wyjde kolumna poza tablice

        if is_sink(u): #sprawdzam czy u-ty wierzcholek jest ujsciem
            return u

        else:
            return 'brak ujscia'

#graf posiadajacy ujscie dla indeksu 3
G = [
    [0,0,1,1,1],
    [0,0,0,1,1],
    [1,0,0,1,1],
    [0,0,0,0,0],
    [0,1,0,1,0],
]
print(universal_sink(G))
