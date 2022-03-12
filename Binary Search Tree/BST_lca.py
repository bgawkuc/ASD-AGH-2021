# Dla zadanych dwóch kluczy: x, y szuka lca (lowest common ancestor), czyli
# wartości klucza, który jest przodkiem zarówno x i y i znajduje się na możliwie
# jak najbliżej liści.

class BST_Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def lowestCommonAncestor(root, x, y):
    while True:
        # oba mniejsze
        if x < root.key and y < root.key:
            root = root.left

        # oba większe
        elif x > root.key and y > root.key:
            root = root.right

        else:
            return root.key
