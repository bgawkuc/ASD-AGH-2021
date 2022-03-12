# Proszę zaimplementować algorytm QuickSort bez użycia rekurencji 

def partition(A, l, r):
    pivot = A[r]
    i = l
    for j in range(l, r):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i


def quickSort(A):
    S = []
    n = len(A)
    l, r = 0, n - 1
    S.append((l, r))

    while len(S) > 0:
        (l, r) = S.pop()
        if l < r:
            q = partition(A, l, r)

            if q - l < r - q:
                S.append((q + 1, r))
                S.append((l, q - 1))
            else:
                S.append((l, q - 1))
                S.append((q + 1, r))
