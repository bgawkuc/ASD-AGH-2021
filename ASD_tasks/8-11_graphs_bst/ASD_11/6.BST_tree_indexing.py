#rozwazamy drzewo BST, które w kazdym węźle zawiera informacje z liczbą węzłów w danym poddrzewie
#a) jak znakeźć i-ty co do wielkości element
#b) wyznaczyc którym co do wielkości w drzewie jest zadany węzeł

#tworze dzrewo BST ale z 2 nowymi polami rozmiar lewego i prawego poddrzewa dla danego Noda
#przy wstawianiu elementow do drzewa aktualizuje rozmiary poddrzew

#a)sprawdzam rozmiar lewego drzewa roota
#jesli lewe drzewo roota + 1 == moje i tzn ze znalazłam odpowiedni klucz, zwracam root.key
#jesli lewe drzewo roota + 1 > mojego i tzn ze i jest mniejsze od idx roota
#musze szukac i w lewym poddrzewie wiec root ustawiam na root.left i powtarzam
#jesli lewe drzewo roota + 1 < mojego i tzn ze i jest wieksze od idx roota
#musze go szukac w prawym poddrzewie, zmniejszam wartosc i o root.leftsize+1, root ustawiam na root.right

#b)szukam mojego klucza za pomocą find i tak znajduje jego miejsce w drzewie
#ustawiam idx na 1 i dodaje do niego wartosc leftsize znalezionego noda
#(bo liczba moj wezel ma > idx od ilosci wezlow w jego lewym poddrzewie)
#i teraz w petli, dopoki node.parent nie bedzie Nonem(czyli dopoki nie dojde do roota)
#jesli node jest prawym dzieckiem to do idx dodaje wartosc jego leftsize+1
#jesi node jest lewym dzieckiem nic nie dodaje
#node zmieniam na node.parent(idę do góry)

class BST_Node:
    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.rightSize = 0
        self.leftSize = 0

#wstawianie elementu do drzewa, dodatkowo inf ile dany węzęł ma podwęzłów
def insert2(root,key,value):
    prev = None
    while root is not None: #szukam liścia do którego mam wstawic element
        if key > root.key:
            root.rightSize += 1
            prev = root
            root = root.right
        else:
            root.leftSize += 1
            prev = root
            root = root.left

    if key < prev.key: #gdy klucz jest mniejszy od mojego liscia o staje sie jego lewym dzieckiem
        prev.left = BST_Node(key,value)
        prev.left.parent = prev #prev staje sie rodzicem mojego nowego Noda
    else:
        prev.right = BST_Node(key,value)
        prev.right.parent = prev


def find(root,key):
    while root is not None:
        if root.key == key:
            return root
        elif key > root.key:
            root = root.right
        else:
            root = root.left
    return None


#a) szukanie i-tego co do wielkosci elementu
#bez rekurencji
def find_ith1(root,i):
    while root is not None:
        if i == (root.leftSize + 1):
            return root.key
        elif i < root.leftSize + 1: #i < rozmiaru lewego poddzrewa + 1 to w nim szukam
            root = root.left
        else: #gdy i > root.leftSize + 1, szykam w prawym poddrzewie
            i -= root.leftSize + 1
            root = root.right
    return None

#sposob z rekurencją
def find_ith2(root,i):
    if root is None:
        return
    cnt = root.leftSize + 1 #rozmiar lewego poddrzewa + 1 to nr kolejnosci roota
    if cnt == i:
        print(root.key)
    elif i < cnt: #gdy i jest mniejsze tzn ze key jest mniejsze od roota
        find_ith2(root.left,i)
    else: #czyli i jest wieksze od roota -> szukam w prawym poddrzewie
        find_ith2(root.right,i-cnt)

#sposob bez uzycia pól left/right-Size
#szukam el minimalnego a potem nastepnika dopoki nie bedzie to i-ta liczba

def getMin(root):
    prev = None
    while root:
        prev = root
        root = root.left
    return prev


def successor(root,k):
    node = find(root,k)
    if node is None:
        return None
    if node.right:
        return getMin(node.right)
    p = node.parent
    while p and p.right == node:
        node = p
        p = p.parent
    return p

def findIth(root,i):
    curr = getMin(root)
    cnt = 1
    while cnt < i:
        curr = successor(root,curr.key)
        cnt += 1
    return curr.key


#b) sprawdzanie który co do wielkości jest podany węzeł
def getIdx(root,key):
    node = find(root,key)
    idx = 1 #zaczynam numerowanie od 1

    #wszystko co jest w jego lewym poddrzewie jest od niego mniejsze
    #wiec dodaje do idx rozmiar jego lewego poddrzewa
    idx += node.leftSize

    #jesli jest to lewe dziecko to ide do góry(do rodzica)
    #a jak prawe to dodaje rozmiar lewego poddrzewa jego rodzica i ide do gory(do rodzica)
    while node.parent is not None:
        if node.parent.right is not None and node.parent.right.key == node.key:
            idx += (node.parent.leftSize + 1)
        node = node.parent
    return idx


root2 = BST_Node(6,1)
insert2(root2,4,1)
insert2(root2,8,1)
insert2(root2,2,1)
insert2(root2,1,1)
insert2(root2,5,1)
insert2(root2,7,1)
insert2(root2,9,1)



find_ith2(root2,3)
print()
print(find_ith1(root2,3))
print()
print(getIdx(root2,4))