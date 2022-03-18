# Inwestor planuje wybudować nowe osiedle akademików. Architekci przedstawili projekty budynków, z których inwestor musi wybrać podzbiór spełniając jego oczekiwania. Każdy budynek
# reprezentowany jest jako prostokąt o pewnej wysokości h, podstawie od punktu a do punktu b,
# oraz cenie budowy w (gdzie h, a, b i w to liczby naturalne, przy czym a < b). W takim budynku
# może mieszkać h ⋅ (b − a) studentów.
# Funkcja powinna zwrócić tablicę z numerami budynków (zgodnie z kolejnością w T, numerowanych
# od 0), które nie zachodzą na siebie, kosztują łącznie mniej niż p i mieszczą maksymalną liczbę
# studentów. Jeśli więcej niż jeden zbiór budynków spełnia warunki zadania, funkcja powinna zwrócić
# zbiór o najmniejszym łącznym koszcie budowy. Dwa budynki nie zachodzą na siebie, jeśli nie mają
# punktu wspólnego.
# Można założyć, że zawsze istnieje rozwiązanie zawierające co najmniej jeden budynek. Funkcja
# powinna być możliwie jak najszybsza i zużywać jak najmniej pomięci.

def people(h, a, b):
    return h * (b - a)


# liczy dla kazdego budynku jaki inny moze byc bezposrednio przed nim
# wybiera ten najblizszy
def previous(A):
    n = len(A)
    p = [None] * n

    for i in range(n):
        for j in range(i):

            if A[j][2] < A[i][1]:
                if p[i] == None or A[j][1] > A[p[i]][1]:
                    p[i] = j
    return p


def selectBuildings(A, p):
    n = len(A)

    for i in range(n):
        new = []
        for j in range(4):
            new.append(A[i][j])
        new.append(i)
        A[i] = new

    A.sort(key=lambda x: x[1])
    prev = previous(A)

    # jaka max ilosc osob zmiesci sie w budynkach do idx i włącznie mając budżet p
    # gdy budynki na siebie nie nachodzą
    dp = [[0] * (p + 1) for _ in range(n)]

    for i in range(A[0][3], p + 1):
        dp[0][i] = people(A[0][0], A[0][1], A[0][2])

    for i in range(1, n):  # idx budynku
        for price in range(1, p + 1):  # aktualna cena
            h, a, b, w, idx = A[i]

            if price < w:
                dp[i][price] = dp[i - 1][price]

            else:
                if prev[i] is not None:
                    dp[i][price] = max(dp[i - 1][price], dp[prev[i]][price - w] + people(h, a, b))
                else:
                    dp[i][price] = max(dp[i - 1][price], people(h, a, b))

    bestCol = 0
    for i in range(p, -1, -1):
        if dp[n - 1][i] >= dp[n - 1][bestCol]:
            bestCol = i

    def getSolution(i, price):
        if i < 0:
            return []
        elif i == 0:
            if A[0][3] <= price:
                return [A[0][4]]
            else:
                return []
        else:
            if dp[i][price] == dp[i - 1][price]:
                return getSolution(i - 1, price)
            else:
                return getSolution(i - 1, price - A[i][3]) + [A[i][4]]

    return sorted(getSolution(n - 1, bestCol)), dp[n - 1][price]


# [0,2,4,5,7]
A = [(1, 8, 12, 5), (4, 7, 8, 2), (3, 2, 3, 6), (9, 7, 8, 5), (8, 21, 22, 8), (5, 4, 7, 10), (1, 21, 24, 10),
     (7, 14, 16, 1)]
P = 32
# [0,2]
A1 = [(2, 1, 5, 3), (3, 7, 9, 2), (2, 8, 11, 1)]
P1 = 5
# [0,1,2,5]
A2 = [(7, 23, 24, 1), (2, 10, 14, 3), (7, 17, 22, 1), (9, 20, 22, 2), (4, 19, 22, 8), (2, 2, 6, 1)]
P2 = 10
# [0,2,3]
A3 = [(8, 2, 6, 2), (9, 4, 8, 5), (9, 8, 9, 2), (3, 10, 15, 1), ]
P3 = 7

print(selectBuildings(A3, P3))
