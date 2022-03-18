# Mamy daną N elementową tablicę T liczb rzeczywistych, w której liczby zostały wygenerowane z pewnego rozkładu losowego. Ten rozkład mamy zadany jako k przedziałów
# [a1, b1],[a2, b2], . . . ,[ak, bk] takich, że i-ty przedział jest wybierany z prawdopodobieństwem ci
# a liczba z przedziału jest wybierana zgodnie z rozkładem jednostajnym. Przedziały mogą na siebie nachodzić, liczby ai
# , bi są liczbami naturalnymi ze zbioru {1, . . . , N}. Proszę zaimplementować
# funkcję SortTab(T,P) sortująca podaną tablicę. Pierwszy argument to tablica do posortowania a
# drugi to opis przedziałów w postaci: P = [(a1, b1, c1), (a2, b2, c2), . . ., (ak, bk, ck)].

def insertionSort(A):
    for i in range(1, len(A)):
        el = A[i]
        j = i - 1
        while j >= 0 and A[j] > el:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = el


def bucketSort(A):
    n = len(A)
    buckets = [[] for _ in range(n)]
    mini = min(A)
    maxi = max(A)
    r = (maxi - mini) / n

    if r == 0:
        return A

    for i in range(n):
        d = ((A[i] - mini) / r) - int((A[i] - mini) / r)

        if d == 0 and A[i] != mini:
            bucketIdx = int((A[i] - mini) / r) - 1
        else:
            bucketIdx = int((A[i] - mini) / r)

        buckets[bucketIdx].append(A[i])

    result = []
    for i in range(n):
        insertionSort(buckets[i])
        result.extend(buckets[i])
    return result


def sortRandom(A, P):
    n = len(A)
    buckets = [[] for _ in range(n)]
    mini = min(A)
    maxi = max(A)
    r = (maxi - mini) / n

    if r == 0:
        return A

    for i in range(n):
        d = ((A[i] - mini) / r) - int((A[i] - mini) / r)

        if d == 0 and A[i] != mini:
            bucketIdx = int((A[i] - mini) / r) - 1
        else:
            bucketIdx = int((A[i] - mini) / r)

        buckets[bucketIdx].append(A[i])

    result = []

    for B in buckets:
        if len(B):
            result.extend(bucketSort(B))
    return result