# Proszę zapropnować algorytm, który oblicza sumę wszystkich wartości w drzewie binarnym zdefiniowanym na węzłach typu:
# class BNode:
#     def __init__( self, key ):
#         self.left = None
#         self.right = None
#         self.parent = None
#         self.key = key
# Program może korzystać wyłącznie ze stałej liczby zmiennych (ale wolno mu zmieniać strukturę drzewa, pod
# warunkiem, że po zakończonych obliczeniach drzewo zostanie przywrócone do stanu początkowego.)


class BNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def getMin(root):
    prev = None
    while root is not None:
        prev = root
        root = root.left
    return prev


def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None


def successor(root, key):
    node = find(root, key)
    if node is None:
        return None

    if node.right is not None:
        return getMin(node.right)

    p = node.parent
    while p is not None and node.key == p.right.key:
        node = p
        p = p.parent

    return p


def sumOfNodes(root):
    sum_ = 0
    mini = getMin(root)
    sum_ += mini.key

    while successor(root, mini.key) is not None:
        mini = successor(root, mini.key)
        sum_ += mini.key

    return sum_