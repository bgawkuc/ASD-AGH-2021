# Znajdź wartość średnią (średnia arytmetyczna) wśród wszystkich kluczy w drzewie.

# Przechodzę po drzewie w kolejności inorder.
# Sumuje wszystkie klucze i liczę ilość.

class BST_Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


def average(root):
    sum_ = 0  # suma kluczy
    cnt = 0  # ilosc węzłów

    def inorder(root):
        nonlocal sum_, cnt
        if root is not None:
            inorder(root.left)
            sum_ += root.key
            cnt += 1
            inorder(root.right)

    inorder(root)
    return sum_ / cnt
