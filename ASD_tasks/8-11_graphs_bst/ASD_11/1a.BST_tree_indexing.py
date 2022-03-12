# Rozważmy drzewa BST, które dodatkowo w każdym węźle zawierają pole z liczbą węzłów w danym poddrzewie.
# Proszę opisać jak w takim drzewie wykonywać następujące operacje:
# 1. znalezienie i-go co do wielkości elementu,
# 2. wyznaczenie, którym co do wielkości w drzewie jest zadany węzeł

class BST_Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.rightSize = 0  # liczba węzłów w prawym poddrzewie
        self.leftSize = 0  # liczba węzłów w lewym poddrzewie


# 1.) szukanie i-tego co do wielkosci elementu
def find_ith(root, i):
    while root is not None:
        if i == (root.leftSize + 1):
            return root.key
        elif i < root.leftSize + 1:
            root = root.left
        else:
            i -= root.leftSize + 1
            root = root.right
    return None


# 2.) sprawdzanie który co do wielkości jest podany węzeł
def getIdx(root, key):
    node = find_ith(root, key)
    idx = 1
    idx += node.leftSize

    while node.parent is not None:
        if node.parent.right is not None and node.parent.right.key == node.key:
            idx += (node.parent.leftSize + 1)
        node = node.parent

    return idx
