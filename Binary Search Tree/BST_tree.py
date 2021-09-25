#binary search tree
#drzewo wyszukiwań binarnych

#to takie drzewo binarne które ma w korzeniu wartość x
#w jego lewym podrzewie są wartości mniejsze a w prawym wieksze
#i w kolejnych podrzewach ta sama zasada funkcjonuje
#szuaknie jest proporocjonalne do wysokosci drzewa- min logn, najgorzej moze sie zrobic liniowa

class BST_Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

#zlozonosc proporcjonalna do wysokosci drzewa
#znajdź element w drzewie, jesli go nie ma zwróć None
def find(root,key):
    while root is not None: #dopoki korzen nie jest Nonem
        if root.key == key: #gdy klucz korzenia jest rowny szukanemu kluczowi
            return root
        elif key < root.key: #gdy szukany klucz jest mniejszy to szukam w leweym poddrzewie
            root = root.left
        else: #gdy szukany klucz jest większy to szukam w prawym poddrzewie
            root = root.right
    return None

#wstawianie elementu do drzewa
#NIE AKTUALIZUJE ON RODZICÓW!
#jak robie drzewo to:
#root = BST(k,v)
#root = insert(root,k1,v1)
#root = insert(root,k2,v2) itd
def insert(root,key,value):
    if root is None:
        return BST_Node(key,value)
    elif root.key < key:
        root.right = insert(root.right,key,value)
    else:
        root.left = insert(root.left,key,value)
    return root

#LEPSZY INSERT BO AKTUALIAZUJE RODZICÓW
#jak robie drzewo to:
#root = BST(k,v)
#insert(root,k1,v1)
#insert(root,k2,v2) itd
def insert2(root,key,value):
    prev = None
    while root is not None: #szukam liścia do którego mam wstawic element
        if key > root.key:
            prev = root
            root = root.right
        else:
            prev = root
            root = root.left

    if key < prev.key: #gdy klucz jest mniejszy od mojego liscia o staje sie jego lewym dzieckiem
        prev.left = BST_Node(key,value)
        prev.left.parent = prev #prev staje sie rodzicem mojego nowego Noda
    else:
        prev.right = BST_Node(key,value)
        prev.right.parent = prev


#usuwanie
def remove(root,key):
    toRemove = find(root,key)

    # tego Noda nie ma w drzewie
    if toRemove is None:
        return

    # gdy nie ma on prawego dziecka
    elif toRemove.right is None:

        #gdy Node nie ma zadnego dziecka(= jest liściem)
        if toRemove.left is None:

            #gdy Node jest lewym dzieckiem
            #tzn sprawdzam czy rodzic ma lewe dziecko i to dziecko jest moim Nodem
            if toRemove.parent.left is not None and toRemove.parent.left.key == key:
                toRemove.parent.left = None #rodzicowi usuwam lewe dziecko

            #gdy Node jest prawym dzieckiem
            else:
                toRemove.parent.right = None #rodzicowi usuwam prawe dziecko

        #gdy Node nie jest liściem, ale nie ma prawego dziecka
        #ma tylko lewe dziecko
        else:

            #gdy jest on dzieckiem lewego rodzica
            #to jego dziecko(lewe) przepinam do lewego rodzica
            if toRemove.parent.left is not None and toRemove.parent.left.key == toRemove.key:
                toRemove.parent.left = toRemove.left

            #gdy jest on dzieckiem prawego rodzica
            #to jego dziecko(lewe) przepinam do prawego rodzica
            elif toRemove.parent.right is not None and toRemove.parent.right.key == toRemove.key:
                toRemove.parent.right = toRemove.left

    #gdy nie ma on lewego dziecka
    elif toRemove.left is None:

        #gdy jest on dzieckiem lewego rodzica
        #to jego dziecko(prawe) przepinam do lewego rodzica
        if toRemove.parent.left is not None and toRemove.parent.left.key == toRemove.key:
            toRemove.parent.left = toRemove.right

        #gdy jest on dzieckiem prawego rodzica
        #to jego dziecko(prawe) przepinam do prawego rodzica
        elif toRemove.parent.right is not None and toRemove.parent.right.key == toRemove.key:
            toRemove.parent.right = toRemove.right

    #gdy ma on oboje dzieci
    else:
        #szukam nastepnika, jego wartosci przepisuje na usuwanego
        #z oryginalnego miejsca, usuwam nastepnika
        succ = successor(root,key)
        Key = succ.key
        Value = succ.value
        remove(root,succ.key) #usuwam nastepnik
        toRemove.key = Key #przepinam wartosci nastepnika do mojego Noda
        toRemove.value = Value

#następnik czyli następna wartość jaka byłaby odwiedzona w drzewie inorder po key
def successor(root,key):
    node = find(root,key)
    if node is None: #brak takiego klucza w drzewie
        return None
    if node.right is not None: #gdy posiada prawe podrzewo to szukam w nim minimum
        return getMin(node.right)
    #w lewym podrzewie przechodze do gory dopoki node jest prawym dzieckiem
    p = node.parent
    while p is not None and node == p.right:
        node = p
        p = p.parent
    return p.key

#poprzednik czyli poprzednia wartosc jaka byłaby odwiedzona w drzewie inorder przed key
def predecessor(root,key):
    node = find(root,key)
    if node is None: #gdy takiego klucza nie ma w drzewie
        return None
    if node.left is not None: #gdy posiada on lewe drzewo to w nim szukam max
        return getMax(node.left)
    #w prawym drzewie przechodze do gory dopoki node jest lewym dzieckiem
    p = node.parent
    while p is not None and node == p.left:
        node = p
        p = p.parent
    return p.key

#znajdz element minimalny
#przechodze w doł po lewych galezaich dopoki root nie bedzie None
#tzn ze prev jest na minimalnej wartosci-lisciu
def getMin(root):
    prev = None
    while root is not None:
        prev = root
        root = root.left
    return prev.key


#znajdź element maksymalny
def getMax(root):
    prev = None
    while root is not None:
        prev = root
        root = root.right
    return prev.key


#LEWY, ROOT, PRAWY
def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print(root.key)
        printInorder(root.right)

#ROOT, LEWY, PRAWY
def printPreorder(root):
    if root is not None:
        print(root.key)
        printPreorder(root.left)
        printPreorder(root.right)

#LEWY, PRAWY, ROOT
def printPostorder(root):
    if root is not None:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.key)


#dostaje klucze z drzewa w porzadku posortowanym
A = []
def inorderToArray(root,A):
    if root is not None:
        inorderToArray(root.left,A)
        A.append(root.key)
        inorderToArray(root.right,A)
    return A

# root = BST_Node(6,1)
# a = BST_Node(4,1)
# b = BST_Node(5,1)
# c = BST_Node(2,1)
# d = BST_Node(3,1)
# g = BST_Node(1,1)
# e = BST_Node(8,1)
# f = BST_Node(9,1)
# h = BST_Node(7,1)
#
# root.left = a
# a.left = c
# a.right = b
# c.left = g
# root.right = e
# e.left = h
# e.right = f

# print(getMax(root))
# print(getMin(root))
# print()
# printInorder(root)
# printPostorder(root)
# printPreorder(root)


root = BST_Node(6,1)
root = insert(root,4,1)
root = insert(root,8,1)
root = insert(root,2,1)
root = insert(root,1,1)
root = insert(root,5,1)
root = insert(root,7,1)
root = insert(root,9,1)
printInorder(root)
print()

print(successor(root,4))
print(predecessor(root,4))