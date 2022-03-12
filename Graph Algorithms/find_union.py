# Struktura find-union (zbiorów rozłącznych).
# Posiada 2 operacje:
# 1) find- znajduje zbiór, w którym znajduje się zadany element
# 2) union - łączy dwa zbiory w jeden

class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0  # wysokość
        self.parent = self  # wskazanie na rodzica


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)

    # do większego zbioru dopinam mniejszy
    if x.rank > y.rank:
        y.parent = x

    elif y.rank > x.rank:
        x.parent = y

    else:
        x.parent = y
        y.rank += 1
