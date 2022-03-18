# Dana jest dwuwymiarowa tablica T o rozmiarach N × N wypełniona liczbami naturalnymi (liczby
# są parami różne). Proszę zaimplementować funkcję Median(T), która przekształca tablicę T, tak
# aby elementy leżące pod główną przekątną nie były większe od elementów na głównej przekątnej,
# a elementy leżące nad główną przekątną nie były mniejsze od elementów na głównej przekątnej.
# Algorytm powinien być jak najszybszy oraz używać jak najmniej pamięci ponad tę, która potrzebna
# jest na przechowywanie danych wejściowych (choć algorytm nie musi działać w miejscu).

def partition(A, l, r):
    piv = A[r]
    i = l
    for j in range(l, r):
        if A[j] <= piv:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i


def quickselect(A, l, r, k):
    q = partition(A, l, r)

    if k == q - l:
        return
    elif k < q - l:
        return quickselect(A, l, q - 1, k)
    else:
        return quickselect(A, q + 1, r, k - (q - l) - 1)


def median(A):
    n = len(A)
    new = []

    for i in range(n):
        for j in range(n):
            new.append(A[i][j])

    # indeks poczatku i konca glownej przekatnej
    start = (n ** 2 - n) // 2
    end = start + (n - 1)

    quickselect(new, 0, n ** 2 - 1, start)
    quickselect(new, start, n ** 2 - 1, end - start)

    # główna przekątna
    idx = start
    for i in range(n):
        A[i][i] = new[idx]
        idx += 1

    # dolny trojkat
    idx = 0
    for i in range(n):
        for j in range(i):
            A[i][j] = new[idx]
            idx += 1

    # górny trójkąt
    idx = end + 1
    for i in range(n):
        for j in range(i + 1, n):
            A[i][j] = new[idx]
            idx += 1

    return A
