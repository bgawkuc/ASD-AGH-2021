# Proszę zaimplementować algorytm QuickSort do sortowania n elementowej tablicy tak, żeby
# zawsze używał najwyżej O(log n) dodatkowej pamięci na stosie, niezależnie od jakości podziałów w funkcji
# partition.


def partition(A, l, r):
    pivot = A[r]
    i = l
    for j in range(l, r):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i


def quicksort(A, l, r):
    while l < r:
        q = partition(A, l, r)
        if q - l < r - q:
            quicksort(A, l, q - 1)
            l = q + 1
        else:
            quicksort(A, q + 1, r)
            r = q - 1