# Proszę zapropnować algorytm, który oblicza sumę wszystkich wartości w drzewie binarnym zdefiniowanym na węzłach typu:
# class BNode:
#     def __init__( self, key ):
#         self.left = None
#         self.right = None
#         self.parent = None
#         self.key = key
# Program może korzystać wyłącznie ze stałej liczby zmiennych (ale wolno mu zmieniać strukturę drzewa, pod
# warunkiem, że po zakończonych obliczeniach drzewo zostanie przywrócone do stanu początkowego.)

#Szukam wartości minimalnego klucza w drzewie i dodaje je do sumy.
#Dopóki istnieje następnik to przechodzę do niego i dodaje go do sumy.

class BNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

#zwraca najmniejszą wartość węzła w drzewie
def getMin(root):
    prev = None
    while root is not None:
        prev = root
        root = root.left
    return prev

#znajduje węzęł o zadanym kluczu
def find(root,key):
    while root is not None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None

#znajduje następnik dla zadanego klucza
def successor(root,key):
    node = find(root,key)
    if node is None:
        return None
    
    if node.right is not None:
        return getMin(node.right)
    
    p = node.parent
    while p is not None and node.key == p.right.key:
        node = p
        p = p.parent
    
    return p

#suma wszystkich węzłów
def sumOfNodes(root):
    sum_ = 0
    mini = getMin(root) 
    sum_ += mini.key
    
    while successor(root,mini.key) is not None: 
        mini = successor(root,mini.key)
        sum_ += mini.key 
    
    return sum_
