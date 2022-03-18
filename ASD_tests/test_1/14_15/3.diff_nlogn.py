# Jak posortować n-elementową tablicę liczb rzeczywistych, które przyjmują tylko log n różnych
# wartości? Uzasadnić poprawność algorytmu i oszacować złożoność. (Nie trzeba implementować).

def binarySearch(A, l, r, x):
    if l <= r:
        mid = l + (r - l) // 2
        if x == A[mid]:
            return True, mid
        elif x < A[mid]:
            return binarySearch(A, l, mid - 1, x)
        else:
            return binarySearch(A, mid + 1, r, x)
    return False, None


def findUniq(A):
    n = len(A)
    uniq = []

    for i in range(n):
        isIn, idx = binarySearch(uniq, 0, len(uniq) - 1, A[i])
        if not isIn:
            uniq.append(A[i])
            uniq.sort()

    return uniq