#Proszę zaimplementować algorytm znajdowania k-go co do wielkości elementu w tablicy
#w n elementowej w “spodziewanym” czasie O(n) na podstawie randomizowanego Partition z QuickSort’a

#Za pomocą algorytmu 'mediany median' szukam elementu, który będzie pivotem.
#Używając quicksorta znajduje k-ty element.

def insertionSort(A, l, r):
    for i in range(l + 1, r + 1):
        el = A[i]
        j = i - 1
        while j >= l and A[j] > el:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = el
    return A


def median(A, l, n):
    r = n + l - 1
    insertionSort(A, l, r)
    return l + (n - 1) // 2


def medianOfMedians(A, l, r):
    n = r - l + 1

    if n % 5 == 0:
        cntMedians = n // 5
    else:
        cntMedians = n // 5 + 1

    i = l
    while i * 5 + 4 < n:
        m = median(A, i * 5, 5)
        A[m], A[i] = A[i], A[m]
        i += 1

    if i * 5 < n:
        m = median(A, i * 5, n % 5)
        A[m], A[i] = A[i], A[m]

    if cntMedians == 1:
        return A[0]
    elif cntMedians <= 5:
        return A[median(A, 0, 5)]
    else:
        return medianOfMedians(A, l, l + cntMedians - 1)


def partition(A, l, r, pivot):
    for i in range(l, r):
        if A[i] == pivot:
            A[i], A[r] = A[r], A[i]
            break

    pivot = A[r]
    i = l

    for j in range(l, r):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[i], A[r] = A[r], A[i]
    return i


def quickSelect(A, l, r, k):
    m = medianOfMedians(A, l, r)
    piv = partition(A, l, r, m)

    if piv - l == k:
        return A[piv]
    elif k < piv - l:
        return quickSelect(A, l, piv - 1, k)
    else:
        return quickSelect(A, piv + 1, r, k - piv + l - 1)


def kthFromArray(A, k):
    return quickSelect(A, 0, len(A) - 1, k)
