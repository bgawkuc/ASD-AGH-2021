#dany jest zbior przedziałow I = {[a1,b1],...[an,bb]}
#przedzial [ai,bi] deaktywuje przedzial [aj.bj] jesli [ai,bi] jest podzbiorem [aj,bj]
#zaproponuje algorytm ktory znajduje pozzdbior I o max rozmiarez
#taki ze zaden przedzial nie jest deaktywowany przez inny
#zwracam najwieksza liczbe rozlacznych podzbiorow(zwracam je dokladnie)

#sortujemy przedzialy po poczatkach
#tworzymy koejke do ktorej  bedziemy dodawac konce przedzialow
#rozwazam kolejne przedzialy
#jesli koniec przedzialu <= od najdalszego konca bedacego w kolejce
#tzn ze ten przdzial go deaktywuje, wiec go usuwamy
#wyciagam kolejny koniec kolejki i dopoki sa >= to usuwamy
#algorytm jest poprawny gdyz gdy znajdziemy przedzial A konczacy sie na naszym aktualnie rozwazanym
#to dzieki posortowaniu po poczatkach mamy pewnosc ze zaczynal sie on przed aktuwalnie rozwazanym
#a wiec jest deaktywowany

def subintervals(A):
    n = len(A)
    #posortowane po początkach
    starts = [[A[i][0],A[i][1],1] for i in range(n)]
    starts.sort(key=lambda x: x[0])

    #lista ta co wyzej tylko posortowana po koncach
    ends = [[starts[i][1],i] for i in range(n)]
    ends.sort(key=lambda s:s[0])
    print(starts)
    print(ends)

    s = 0
    e = 0
    res = []

    while s < len(starts) and e < len(ends):
        end = ends[e]

        if starts[end[1]][2] == 1: #gdy poczatek nie byl uzyty

            if end[1] == s: #gdy indeks startu odpowiada indeksowi konca(czyli mam poczatek i koniec 1 przedzialu)

                while s + 1 < len(starts) and e < len(ends) and starts[s+1][1] == end[0]: #gdy koniec kolejnej czynnosci jest = koncowi obcenej
                    starts[s][2] = 0
                    e += 1
                    s += 1
                res.append(starts[s])
                e += 1

            else:
                starts[s][2] = 0

        else:
            e += 1

        if starts[end[1]][2] != 0:
            s += 1

    return res

intervals = [(0, 2), (1, 2), (2, 3), (5, 9), (5, 7), (7, 8), (8, 10)]
intervals1 = [(0, 2), (1, 2), (2, 3), (5, 9), (5, 7)]
intervals2 = [(0, 10), (1, 9), (2, 7), (2, 5), (3, 5), (4, 4)]
print(subintervals(intervals1))


