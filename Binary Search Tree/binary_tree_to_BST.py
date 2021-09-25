#mam drzewo binarne
#mam je przekształcic w BST

#wyciagam klucze, sortuje je rosnaco
#nastepnie rekurencyjnie tworze drzewo

class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

#wujmyje klucze
def extractKeys(root,A):
    if root is None:
        return
    extractKeys(root.left,A)
    A.append(root.key)
    extractKeys(root.right,A)

#na bazie tablicy z kluczami tworze drzewo
def convertToBST(root,A):
    if root is None:
        return
    convertToBST(root.left,A)
    root.key = next(A)
    convertToBST(root.right,A)

root = Node(8)
root.left = Node(3)
root.right = Node(2)
root.right.left = Node(9)
root.right.right = Node(10)


A = []
extractKeys(root,A)
A.sort()
A = iter(A)
convertToBST(root,A)

#sprawdzam czu dbrze zadziałało
print(root.key)
print(root.left.key)
print(root.right.key)
print(root.right.right.key)
print(root.right.left.key)


#2 SPOSÓB NA IMPLEMENTACJE
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

    #na bazie tablicy A tworzE drzwo BST taką samą procedurą co inorder
    def func(root):
        nonlocal idx
        if root is None:
            return
        func(root.left)
        root.key = A[idx]
        idx += 1
        func(root.right)

    return func(root)


root1 = Node(2)
root1.left = Node(5)
root1.right = Node(1)
root1.left.left = Node(8)
root1.left.right = Node(7)
root1.right.left = Node(6)
convert2BST(root1)


