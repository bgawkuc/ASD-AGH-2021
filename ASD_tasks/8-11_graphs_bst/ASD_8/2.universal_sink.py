# Mówimy, że wierzchołek t w grafie skierowanym jest uniwersalnym ujściem, jeśli:
# (a) z każdego innego wierzchołka v istnieje krawędź z v do t
# (b) nie istnieje żadna krawędź wychodząca z t.
# Podaj algorytm znajdujący uniwersalne ujście (jeśli istnieje) przy reprezentacji macierzowej.

#Szukam takiego wierzchołka u, dla którego cały wiersz G[u] ma wypełniony wartością 0, a kolumna jest cała wypełniona 1 (poza G[u][u]).
#Szukam potencjalnego wierzchołka w grafie, który mógłby być ujściem poruszając się w prawo/ w dół w zależności od wartości.
#Za pomocą DFS sprawdzam czy jest ujściem.
#Złożoność: O(V)

def universal_sink(G):
    n = len(G)
    # u-wiersz,v-kulumna
    u, v = 0, 0

    while u < n and v < n:
        if G[u][v] == 0:
            v += 1
        else:
            u += 1

    if u == n:
        return 'brak ujscia'

    def is_sink(u):
        for v in range(n):
            if G[u][v] == 1:
                return False
            if u != v and G[v][u] == 0:
                return False

        return True

    if is_sink(u):
        return u
    else:
        return 'brak ujscia'
