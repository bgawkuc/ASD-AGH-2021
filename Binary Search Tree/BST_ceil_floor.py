# Dla zadanej wartości key znajduje suift i podłogę.
# Sufit jest możliwie jak najmniejszą wartością, która jest większa lub równa od key.
# Podłoga jest możliwie jak największą wartością, która jest mniejsza lub równa od key.


class BST_Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def find(root, key):
    ceil, floor = None, None

    while root is not None:
        if key == root.key:
            return "floor", key, "ceil", key

        elif key < root.key:
            ceil = root.key
            root = root.left

        else:
            floor = root.key
            root = root.right

    return "floor:", floor, "ceil:", ceil
