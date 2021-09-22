#Proszę zaimplementować algorytm znajdowania k-go co do wielkości elementu w tablicy
#w n elementowej w “spodziewanym” czasie O(n) na podstawie randomizowanego Partition z QuickSort’a
#korzystam z algorytmu magicznych piatek
#w ten sposob znajduje mediane median
#staje sie ona pivotem
#w qsorcie: gdy indkes k = indeks q -> zwracam t[q]
#gdy ind k < ind q -> szukam w lewej czesci tab
#gdy ind k > ind q -> szukam w prawej czesci tab
from random import randint, shuffle, seed
from time import time

def insertionSort(A, l, r):
    for i in range(l + 1, r + 1):
        el = A[i]
        j = i - 1
        while j >= l and A[j] > el:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = el

def median(A, l, n):
    r = l + n - 1
    insertionSort(A, l, r)
    return l + (n - 1) // 2

def medianOfMedians(A, l, r, k):
    n = r - l + 1

    if n % 5 == 0:
        cntMed = n // 5
    else:
        cntMed = n // 5 + 1

    i = l
    while i * 5 + 4 < n:
        m = median(A, i * 5, 5)
        A[m], A[i] = A[i], A[m]
        i += 1

    if i * 5 < n:
        m = median(A, i * 5, n % 5)
        A[m], A[i] = A[i], A[m]

    if cntMed == 1:
        return 0
    elif cntMed < 6:
        return median(A, l, cntMed)
    else:
        return medianOfMedians(A, l, l + cntMed - 1,k)

def partition(A, l, r, pivot):
    for i in range(l, r):
        if A[i] == pivot:
            A[i], A[r] = A[r], A[i]
            break

    pivot = A[r]
    i = l - 1

    for j in range(l, r):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quickSelect(A,l,r,k):
    m = medianOfMedians(A,l,r,k)
    q = partition(A, l, r, A[m])

    if q - l == k:
        return A[q]
    elif k < q - l:
        return quickSelect(A, l, q - 1, k)
    else:
        return quickSelect(A, q + 1, r, k - q + l - 1)

def linearselect(A, k):
    return quickSelect(A, 0, len(A) - 1, k)

A = [9,0,2,3,7,6,1]
print(linearselect(A,4))


start = time()
seed(42)

n = 1000
for i in range(n):
    A = list(range(n))
    shuffle(A)
    # print(A)
    # print('i',i)
    x = linearselect(A, i)
    # print('x',x)
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)

print("OK")
end = time()
print(end - start)
