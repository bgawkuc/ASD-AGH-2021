# Dane jest drzewo ukorzenione T, gdzie każdy wierzchołek v ma— potencjalnie ujemną—wartość value(v).
# Proszę zaproponować algorytm, który znajduje wartość najbardziej wartościowej ścieżki w drzewie T.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.bestPath = 0


def findBestPath(v):
    if v == None:
        return (0, 0)

    bestL, L = findBestPath(v.left)
    bestR, R = findBestPath(v.right)

    # dlg najlepszej sciezki zakorzenionej w v
    v.bestPath = max(0, v.val, v.val + L, v.val + R)

    # najlepsza sciezka w calym drzewie
    best = max(v.bestPath, bestL, bestR, L + R + v.val)

    return (best, v.bestPath)


def returnBestPath(v):
    return max(findBestPath(v))
