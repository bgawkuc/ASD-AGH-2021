# Sprawdź czy zadane drzewo spełnia warunki na BST.

class BST_Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def isBST(root):
    if root is None or (root.left is None and root.right is None):
        return True

    # gdy lewe dziecko jest wieksze od rodzica to nie jest to BST
    if root.left is not None and root.left.key > root.key:
        return False
    # gdy prawe dziecko jest mniejsze od rodzica to nie jest to BST
    if root.right is not None and root.right.key < root.key:
        return False

    return isBST(root.left) and isBST(root.right)
