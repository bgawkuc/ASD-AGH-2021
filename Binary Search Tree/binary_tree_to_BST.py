#Drzewo binarne przekształca w BST.

#Zapisuje wszystkie klucze z drzewa binarnego w tablicy i sortuje je rosnąco.
#Na bazie tej tablicy tworzę BST.

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def inorder(root):
    A = []
    def func(root):
        if root is not None:
            func(root.left)
            A.append(root.key)
            func(root.right)
    func(root)
    return A

def convert2BST(root):
    #spisuje tablice inorder i ją sortuje
    A = inorder(root)
    A.sort()
    idx = 0

    def func(root):
        nonlocal idx
        if root is None:
            return
        
        func(root.left)
        root.key = A[idx]
        idx += 1
        func(root.right)

    return func(root)
