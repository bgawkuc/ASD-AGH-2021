# Dane jest drzewo binarne T, gdzie każda krawędź ma pewną wartość. Proszę zaimplementować
# funkcję:
# def valuableTree(T, k):
# ...
# która zwraca maksymalną sumę wartości k krawędzi tworzących spójne poddrzewo drzewa T.
# Funkcja powinna być jak najszybsza. Proszę oszacować złożoność czasową oraz pamięciową zastosowanego algorytmu.
# Drzewo T reprezentowane jest przez obiekty klasy Node:
# class Node:
# def __init__(self):
# self.left = None # lewe poddrzewo
# self.leftval = 0 # wartość krawędzi do lewego poddrzewa jeśli istnieje
# self.right = None # prawe poddrzewo
# self.rightval = 0 # wartość krawędzi do prawego poddrzewa jeśli istnieje
# self.X = None # miejsce na dodatkowe dane
# Pole X można wykorzystać do przechowywania dodatkowych informacji w trakcie obliczeń.

from math import inf


class Node:
    def __init__(self):
        self.left = None
        self.leftval = 0
        self.right = None
        self.rightval = 0
        self.path = 0
        self.X = None


def subTree(T, k, maxk):
    if T.X is None:
        T.X = [-1] * (maxk + 1)

    if T.X[k] != -1:
        return T.X[k]

    v = -inf
    if k > 0:
        if T.left is not None:
            v = max(v, subTree(T.left, k, maxk))
            v = max(v, subTree(T.left, k - 1, maxk) + T.leftval)

        if T.right is not None:
            v = max(v, subTree(T.right, k, maxk))
            v = max(v, subTree(T.right, k - 1, maxk) + T.rightval)

        if T.left is not None and T.right is not None:
            for x in range(k - 1):
                v = max(v, subTree(T.left, x, maxk) + T.leftval + subTree(T.right, k - 2 - x, maxk) + T.rigtval)

    elif k == 0:
        v = 0

    T.X[k] = v
    return v


def valuableTree(T, k):
    return subTree(T, k, k)
