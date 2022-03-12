# zlożoność: O(nlogn)


def partition(A, l, r):
    piv = A[r]
    i = l

    for j in range(l, r):
        if A[j] <= piv:
            A[j], A[i] = A[i], A[j]
            i += 1

    A[i], A[r] = A[r], A[i]
    return i


def quicksort(A, l, r):
    if l < r:
        piv = partition(A, l, r)
        quicksort(A, l, piv - 1)
        quicksort(A, piv + 1, r)
    return A
