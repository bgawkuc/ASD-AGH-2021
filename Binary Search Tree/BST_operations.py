# BST - binary search tree
# Drzewo binarne, w którym lewe poddrzewo zawiera mniejsze klucze od korzenia,
# a prawe podrzewo większe.

# Operacje:
# 1) find-sprawdza czy w drzewie znajduje się węzeł o zadanym kluczu
# 2) insert- dodaje węzeł do drzewa o zadanej wartości
# 3) getMin - znajduje wartość minmalnego klucza w drzewie
# 4) getMax - znajduje wartość maksymalnego klucza w drzewie
# 5) successor - znajduje następnik dla węzła o zadanym kluczu
# 6) predecessor - znajduje poprzędnik dla węzła o zadanym kluczu
# 7) printInorder - wypisuje klucze drzewa w kolejnośći: lewy, korzeń, prawy
# 8) printPreorder - wypisuje klucze drzewa w kolejnośći: korzeń, lewy, prawy
# 7) printPostorder - wypisuje klucze drzewa w kolejnośći: lewy, prawy, korzeń

class BST_Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


# 1) sprawdza czy w drzewie znajduje się węzeł o kluczu key
def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None


# 2) dodaje do drzewa węzeł o kluczu key
def insert(root, key):
    prev = None
    while root is not None:
        if key > root.key:
            prev = root
            root = root.right
        else:
            prev = root
            root = root.left

    if key < prev.key:
        prev.left = BST_Node(key)
        prev.left.parent = prev
    else:
        prev.right = BST_Node(key)
        prev.right.parent = prev


# 3) znajdz element minimalny
def getMin(root):
    prev = None
    while root is not None:
        prev = root
        root = root.left
    return prev.key


# 4) znajdź element maksymalny
def getMax(root):
    prev = None
    while root is not None:
        prev = root
        root = root.right
    return prev.key


# 5) znajduje następnik dla węzła o kluczu key
def successor(root, key):
    node = find(root, key)
    if node is None:
        return None
    if node.right is not None:
        return getMin(node.right)
    p = node.parent
    while p is not None and node == p.right:
        node = p
        p = p.parent
    return p.key


# 6) znajduje poprzednik, dla węzła o kluczu key
def predecessor(root, key):
    node = find(root, key)
    if node is None:
        return None
    if node.left is not None:
        return getMax(node.left)
    p = node.parent
    while p is not None and node == p.left:
        node = p
        p = p.parent
    return p.key


# 7) kolejność: LEWY, ROOT, PRAWY
def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print(root.key)
        printInorder(root.right)


# 8) kolejność: ROOT, LEWY, PRAWY
def printPreorder(root):
    if root is not None:
        print(root.key)
        printPreorder(root.left)
        printPreorder(root.right)


# 9) kolejność: LEWY, PRAWY, ROOT
def printPostorder(root):
    if root is not None:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.key)