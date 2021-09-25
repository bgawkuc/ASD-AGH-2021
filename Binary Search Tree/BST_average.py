#znajdz srednią wartosc w BST
#czyli nalezy zsumowac klucze i podzielic sume przez ich ilość

#licze sume i ilosc wezlów za pomocą rekurenycjnej funkcji inorder(tylko nie tworze tablicy z kluczami)
#a po prostu sumuje klucze i zliczma ich ilosc

class BST_Node:
    def __init__(self,key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def insert(root,key):
    prev = None
    while root is not None: #szukam liścia do którego mam wstawic element
        if key > root.key:
            prev = root
            root = root.right
        else:
            prev = root
            root = root.left

    if key < prev.key: #gdy klucz jest mniejszy od mojego liscia o staje sie jego lewym dzieckiem
        prev.left = BST_Node(key)
        prev.left.parent = prev #prev staje sie rodzicem mojego nowego Noda
    else:
        prev.right = BST_Node(key)
        prev.right.parent = prev


def average(root):
    sum_ = 0 #suma kluczy
    cnt = 0 #ilosc węzłów

    #inorder to funkcja do wyswietlania w kolejknosci: lewy, root, prawy
    #modyfikuje ją tak by liczyc sume kluczy i ilosc wezlów
    def inorder(root):
        nonlocal sum_,cnt
        if root is not None:
            inorder(root.left)
            sum_ += root.key
            cnt += 1
            inorder(root.right)

    inorder(root)
    return sum_/cnt

root = BST_Node(6)
insert(root,4)
insert(root,8)
insert(root,2)
insert(root,1)
insert(root,5)
insert(root,7)
insert(root,9)
print(average(root))
