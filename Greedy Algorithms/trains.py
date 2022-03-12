# Dostajesz na wejściu tablicę A, która zawiera krotki z informacjami na temat godziny przyjazdu i odjazdu pociągu.
# Na dworcu znajduje się m peronów. Każdy pociąg musi wjechać na peron o swojej godzinie przyjazdu oraz wyjeżdza
# z niego o godzinie wyjazdu. Sprawdź czy m peronów to wystarczająca ilość dla pociągów z tablicy A.

def trains(A, m):
    n = len(A)
    if n <= m: return True

    A.sort(key=lambda x: x[0])
    platform = [None] * m

    # pierwsze m pociagow wpuszczam na perony
    for i in range(m):
        platform[i] = A[i]

    for i in range(m, n):
        possible = False

        for j in range(m):

            if platform[j][1] <= A[i][0]:
                platform[j] = A[i]
                possible = True
                break

        if possible == False:
            return False

    return True
