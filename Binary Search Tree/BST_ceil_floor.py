#mamy drzewo BST
#dla podanego klucza mam znaleźć jego sufit i podłogę
#gdy klucz znajduje sie w drzewie to sufit i podłoga mają wartość tego klucza
#a gdy nie to trzeba ich poszukac
#wtedy podłoga to najwiekszy z mniejszych kluczy
#a sufit to najmniejszy z wartosci wiekszych

#modyfikuje operacje find
#gdy znajde klucz o wartosci key to go zwracam jako sufit i podłoga
#jesli key > root.key to wartosc PODŁOGI ustawiam na root.key
#bo teraz bede szukac w wiekszych wartosciach, wiec jako podloge mogę ustawic tę wartosc bo jest mniejsza od klucza
#jesli key < root.key to wartość SUFITU ustawiam na root.key
#a skoro teraz bede szukac w mniejszych wartoscach to tę wartosc moge ustawic na sufiy bo jest wieksza od key



class BST_Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def insert(root,key):
    prev = None
    while root is not None:
        if key < root.key:
            prev = root
            root = root.left
        else:
            prev = root
            root = root.right

    if key < prev.key:
        prev.left = BST_Node(key)
        prev.left.parent = prev
    else:
        prev.right = BST_Node(key)
        prev.right.parent = prev


def find(root,key):
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
    return "floor:",floor,"ceil:", ceil


root = BST_Node(6)
insert(root,4)
insert(root,8)
insert(root,2)
insert(root,1)
insert(root,5)
insert(root,7)
insert(root,9)
print(find(root,3))
