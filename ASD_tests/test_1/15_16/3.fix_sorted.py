# Proszę zaimplementować funkcję void SumSort(int A[], int B[], int n). Funkcja ta
# przyjmuje na wejściu dwie n^2-elementowe tablice (A i B) i zapisuje w tablicy B taką permutację
# elementów z A, że:
# suma el w B (idx od 0 do n-1) <= suma el w B (idx od n do 2n-1) <= ... <= suma el w B (idx od n^2-n do n^2 -1)

def insertionSort(T):
    for i in range(1, len(T)):
        el = T[i][1]
        inEl = T[i][0]
        j = i - 1
        while j >= 0 and T[j][1] > el:
            T[j + 1][1] = T[j][1]
            T[j + 1][0] = T[j][0]
            j -= 1
        T[j + 1][1] = el
        T[j + 1][0] = inEl
    return T


def divide(T, n):
    nSum = [[None, 0] for _ in range(n)]
    cnt, newSum, j = n, 0, 0

    for i in range(len(T)):
        if cnt:
            cnt -= 1
            newSum += T[i]
        if cnt == 0:
            nSum[j][0] = i - n + 1
            nSum[j][1] = newSum
            newSum, cnt = 0, n
            j += 1

    insertionSort(nSum)
    return nSum


def sumSorting(T, n):
    new = [0] * len(T)
    nSum = divide(T, n)

    for k in range(n):
        index = nSum[k][0]
        for l in range(n):
            new[k * n + l] = T[index + l]

    return new


t1 = [16, 10, 19, 11, 20, 17, 1, 4, 14, 8, 9, 4, 6, 5, 14, 23]
print(sumSorting(t1, 4))
