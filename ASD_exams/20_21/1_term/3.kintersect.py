# Dany jest zbiór przedziałów A = {(a0, b0), . . . , (an−1, bn−1)}. Proszę zaimplementować funkcję:
# def kintersect( A, k ):
# ...
# która wyznacza k przedziałów, których przecięcie jest jak najdłuższym przedziałem. Zbiór A jest
# reprezentowany jako lista par. Końce przedziałów to liczby całkowite. Można założyć, że k ≥ 1 oraz
# k jest mniejsze lub równe łącznej liczbie przedziałów w A. Funkcja powinna zwracać listę numerów
# przedziałów, które należą do rozwiązania.
# Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową
# użytego algorytmu

# złożoność: O(n^2)


def kintersect(A, k):
    n = len(A)
    inf = float('inf')
    for i in range(n):
        A[i] = [A[i][0], A[i][1], i]

    A.sort(key=lambda x: x[1], reverse=True)
    # zbiór indeksów przedziałów o największym przecięciu
    best = []
    # rozmiar najlepszego przecięcia
    diff = -inf

    # wybieram pierwszy przedział
    for first in range(n):
        s, e, idx = A[first]
        curr = [s, e]
        cnt = 1
        res = [idx]

        # szukam kolejnych k-1 przedziałów
        for new in range(n):

            # start,koniec przedziału,idx w wejsciowej tab
            newS, newE, newIdx = A[new]
            if newIdx not in res and cnt < k:
                if newS <= s:
                    cnt += 1
                    res.append(newIdx)
                    curr = [max(curr[0], newS), min(curr[1], newE)]

            # jak znajde k przedziałów
            if cnt == k:
                # sprawdzam czy ich przecięcie jest większe od ostatnio zapisanego
                if curr[1] - curr[0] > diff:
                    diff = curr[1] - curr[0]
                    best = res[:]
                    break
    return best


# [0, 1, 3]
A = [(0, 4), (1, 10), (6, 7), (2, 8)]
print(kintersect(A, 3))
