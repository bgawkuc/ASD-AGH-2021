# Zadanie 2. Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
# podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
# wzrostu. Proszę zaimplementować funkcję:
# section(T,p,q), która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.

from random import randint


def random_pivot(l, r):
    ind = randint(l, r)
    return ind


def partition(T, l, r):
    ind = random_pivot(l, r)
    pivot = T[ind]
    T[ind], T[r] = T[r], T[ind]
    i = l - 1

    for j in range(l, r):
        if T[j] > pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def quickSelect(T, k, l, r):
    if l <= r:
        i = partition(T, l, r)
        if k == i - l:
            return i
        elif k < i - l:
            return quickSelect(T, k, l, i - 1)
        else:
            return quickSelect(T, k - i - 1 + l, i + 1, r)


def section(T, p, q):
    x = quickSelect(T, p, 0, len(T) - 1)
    y = quickSelect(T, q - x, x, len(T) - 1)
    return T[x:y + 1]


t = [1.6, 1.7, 1.3, 2.0, 1.9, 1.8, 1.6, 1.7]
print(section(t, 2, 3))
