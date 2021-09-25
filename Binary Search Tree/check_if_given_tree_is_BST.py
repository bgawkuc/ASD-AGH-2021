#dostaje na wejsciu drzewo binarne
#sprawdź czy jest to drzewo BST

#tzn mam sprawdzic czy lewe dziecko jest mniejsze od rodzica a prawe wieksze
#i czy zachodzi to na kazdym etapie
#funkcja rekurencyjna
#dla roota sprawdzam:
#jesli on jest Nonem to zwracam True
#jesli lewe dziecko > rodzica to zwracam False
#jesli prawe dziecko < rodzica to zwracam False
#zwracam wywolanie rekurencyjne dla lewego i prawego poddzrewa


class BST_Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def isBST(root):
    #gdy root jest Nonem albo nie ma zadnych dzieci
    if root is None or root.left is None and root.right is None:
        return True

    #gdy lewe dziecko jest wieksze od rodzica to False
    if root.left is not None and root.left.key > root.key:
        return False
    #gdy prawe dziecko jest mniejsze od rodzica to falsz
    if root.right is not None and root.right.key < root.key:
        return False

    #wywoluje dla lewego i prawego poddzrewa
    #oba musza byc True by funkcja zwrocila True
    return isBST(root.left) and isBST(root.right)


root = BST_Node(6)
a = BST_Node(1)
b = BST_Node(3)
c = BST_Node(5)
d = BST_Node(7)

root.left = c
root.right = d
c.left = b
b.right= a #ma byc b.left = a by było bst
print(isBST(root))
