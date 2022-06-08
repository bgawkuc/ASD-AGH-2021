# Dane jest drzewo BST zbudowane z węzłów
# class BNode:
# def __init__( self, value ):
# self.left = None
# self.right = None
# self.parent = None
# self.value = value

# Klucze w tym drzewie znajdują się w polach value i są liczbami całkowitymi. Mogą zatem mieć
# wartości zarówno dodatnie, jak i ujemne. Proszę napisać funkcję, która zwraca wartość będącą
# minimalną możliwą sumą kluczy zbioru wierzchołków oddzielających wszystkie liście od korzenia
# w taki sposób, że na każdej ścieżce od korzenia do liścia znajduje się dokładnie jeden wierzchołek z
# tego zbioru. Zakładamy że korzeń danego drzewa nie jest bezpośrednio połączony z żadnym liściem
# (ścieżka od korzenia do każdego liścia prowadzi przez co najmniej jeden dodatkowy węzeł). Jako
# liść jest rozumiany węzeł W typu BNode such that W.left = W.right = None.
# Rozwiązanie należy zaimplementować w postaci funkcji:
# def cutthetree(T):
# ...
# która przyjmuje korzeń danego drzewa BST i zwraca wartość rozwiązania. Nie wolno zmieniać
# definicji class BNode.


from math import inf


class BNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def isLeaf(v):
    if v.left is None and v.right is None:
        return True
    return False


def cutTheTree(root):
    def cut(v):
        if v is None:
            return 0
        if isLeaf(v):
            return inf

        return min(v.value, cut(v.left) + cut(v.right))

    return cut(root.left) + cut(root.right)


def dodaj(T, key):
    W = BNode(key)
    if key < T.value:
        if T.left == None:
            T.left = W
            W.parent = T
        else:
            dodaj(T.left, key)
    else:
        if T.right == None:
            T.right = W
            W.parent = T
        else:
            dodaj(T.right, key)


def createtree(keys):
    T = BNode(keys[0])
    for i in range(1, len(keys)):
        dodaj(T, keys[i])
    return T


# 3
A = [1, -1, -2, 4, 5, 6, 7]
# 8
A1 = [5, 2, 1, 6, 7, 8]
# 2
A2 = [0, -2, -3, -1, 4, 3, 5]
# 1
A3 = [5, 6, 7, 10, 8, 11, 3, -1, -5, -10, -2]
# 14
A4 = [10, 3, 15, 11, 17, -1, -5, 0]
print(cutTheTree(createtree(A4)))
