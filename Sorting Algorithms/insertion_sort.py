# sortowanie przez wstawianie
# złożoność: O(n^2)

def insertionSort(A):
    for i in range(1, len(A)):
        el = A[i]
        j = i - 1
        while el < A[j] and j >= 0:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = el
    return A
