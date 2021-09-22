#mam ciąg przedziałów domkniętych [a1, b1], . . . ,[an, bn].
#podaj algorytm, który znajduje taki przedział [at, bt], w którym w całości
#zawiera się jak najwięcej innych przedziałów.

def partition(A, l, r, k):
    pivot = A[r][k]
    i = l
    for j in range(l, r):
        if A[j][k] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i


# k-indeks po jakim sortuje
def quicksort(A, l, r, k):
    if l < r:
        q = partition(A, l, r, k)
        quicksort(A, l, q - 1, k)
        quicksort(A, q + 1, r, k)
    return A


def func(A):
    n = len(A)
    # dodaje informacje o indeksie w A
    for i in range(n):
        A[i].append(i)

    # startX/endY-listy z przedzialami posortowana po poczatkach/po koncach
    startX = quicksort(A[:], 0, n - 1, 0)
    endY = quicksort(A[:], 0, n - 1, 1)

    x = [0] * n
    y = [0] * n

    # wypelniam tablice x,y
    for i in range(n):
        #który z kolei (w posortowanej po początkach tablicy)
        #jest przedział który w wejsciowej tablicy miał indeks startX[i][2]
        x[startX[i][2]] = i
        # który z kolei (w posortowanej po końcach tablicy)
        # jest przedział który w wejsciowej tablicy miał indeks endY[i][2]
        y[endY[i][2]] = i

    # diff-ilosc przedzialow jakie sie zawiera w i-tym indeksie
    diff = [0] * n

    maxi = -float("inf")
    maxiIdx = float('inf')

    for i in range(n):
        diff[i] = y[i] - x[i]
        if diff[i] > maxi:
            maxiIdx = i
            maxi = diff[i]

    return A[maxiIdx][:2]
