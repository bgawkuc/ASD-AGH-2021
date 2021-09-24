#prosze zaproponowac algorytm króty oblicza sume wszytskich nodów w drzewie BST
#ale uzywa stałej ilości pamięci(czyli nie mozna dodac zadnego pola)
#pomysł z dodaniem pola move jest dobry tylko to jest UŻYCIE DODATKOWEJ PAMIĘCI

#kazdy node dostaje dodatkowe pole move które informuje gdzie idziemy z niego
#domyslnie pola move maja wartosc left
#gdy przyjde z polem left to ustalam je na right
#gdy przyjde z polem right to ustawiam je na parent
#gdy przyjde z polem parent to wracam sie do góry
#dodajemy do sumy warosc pola wtw gdy move jest ustawione na left

#tworze pętle nieskończoną z 3 ifami
#1) gdy root.move == left; to wtedy do sumy dodaje wartosc tego roota
#root.move ustawiam na right i jesli istnieje root.left to root = root.left
#2) gdy root.move == right,
#root.move ustawiam na parent i jesli istnieje toor.right to root = root.right
#3) gdy root.right == parent
# gdyby root byl tym samym rootem co głowny root to wychodze z pętli to zwracam wynik
#a jak nie to przechodze do góry, do rodzica


#algorytm zadziała dla kazdego drzewa binarnego, niekoniecznie tylko dla BST

#gdy moge uzywac dodatkowej pamięci(koszt węzła move)
class BST_Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.move = "left" #domyslnie left, pojawi sie tez right, parent


def insert(root,key,value):
    prev = None
    while root is not None:
        if key > root.key:
            prev = root
            root = root.right
        else:
            prev = root
            root = root.left

    if key < prev.key:
        prev.left = BST_Node(key,value)
        prev.left.parent = prev #prev staje sie rodzicem mojego nowego Noda
    else:
        prev.right = BST_Node(key,value)
        prev.right.parent = prev


def sumOfNodes(root):
    mainRoot = root #zapamietuje głownego roota
    sum_ = 0

    while True:

        if root.move == "left": #gdy z roota ide do lewego dziecka
            sum_ += root.key #to dodaje do sumy wartość roota
            root.move = "right" #ustawiam kolejny ruch roota
            if root.left is not None: #gdy ma on lewe dziecko to będę iść do niego
                root = root.left

        elif root.move == "right": #gdy z roota ide do prawego dziecka
            root.move = "parent" #ustawiam kolejny ruch roota
            if root.right is not None:
                root = root.right

        elif root.move == "parent": #gdy z roota weszłam do jego dzieci to sie cofam do rodzica
            # gdy wroce do głownego roota i ma on status parent
            #czyli weszłam do niego 3 raz
            if root is mainRoot:
                return sum_
            root = root.parent #wracam sie do gory


root = BST_Node(6,1)
insert(root,1,1)
insert(root,2,1)
insert(root,7,1)
insert(root,4,1)
insert(root,8,1)
insert(root,9,1)

print(sumOfNodes(root))


#2-sposob gdy nie uzywam dodatkowej pamięci
#szukam minimum a potem w pętli szukam następnika i dodaje go do sumy

#bez dodatkowe pola move
class BST_Node2:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

#zwykly insert
def insert2(root,key):
    prev = None
    while root is not None:
        if key < root.key:
            prev = root
            root = root.left
        else:
            prev = root
            root = root.right
    if key < prev.key:
        prev.left = BST_Node2(key)
        prev.left.parent = prev
    else:
        prev.right = BST_Node2(key)
        prev.right.parent = prev

#zwraca min węzęł
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
    # dopoki node jest prawym dzieckiem rodzica
    while p is not None and node.key == p.right.key:
        node = p
        p = p.parent
    return p

#suma wszystkich węzłów
def sumOfNodes2(root):
    sum_ = 0
    mini = getMin(root) #szuka minimum
    sum_ += mini.key
    while successor(root,mini.key) is not None: #dopoki istnieje następnik
        mini = successor(root,mini.key)
        sum_ += mini.key #to dodaje wartosc następnika do sumy
    return sum_

root2 = BST_Node2(6)
insert2(root2,1)
insert2(root2,2)
insert2(root2,7)
insert2(root2,4)
insert2(root2,8)
insert2(root2,9)
print(sumOfNodes2(root2))

#3-gdy nie posiadam pola parent i nie moge uzywac dodatkowej pamięci
#sprawdzam czy moj obecny root ma lewe dziecko
#NIE MA- dodaje wartosc roota do do sumy i przechodze w jego prawe dziecko
#JEST-szukam jego poprzednika, poprzednik dostaje wskazanie na roota i ide w lewo
#to jest tworzenie takich krawedzi wstecznych
#gdyby okazalo sie ze funkcja znajdzie mi wiekszego poprzednik niz root tzn ze przeszłam po krawedzi wstecznej
#wtedy dodaje wartosc roota i ide w prawo
#gdy okaze sie ze Node nie ma zadnego dziecka to dodaje jego klucz do sumy i zwracam ją
#bo to ostatni el w moim drzewie


class BST_Node3:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    def printing(self):
        print(self.key)

def insert3(root,key):
    prev = None
    while root is not None:
        if key < root.key:
            prev = root
            root = root.left
        else:
            prev = root
            root = root.right

    if key < prev.key:
        prev.left = BST_Node3(key)
        prev.left.parent = prev
    else:
        prev.right = BST_Node3(key)
        prev.right.parent = prev

def getMax(root):
    prev = None
    while root is not None:
        prev = root
        root = root.right
    return prev

def find3(root,key):
    while root is not None:
        if key == root.key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None

#poprzednik
def predecessor3(root,key):
    node = find3(root,key)
    if node is None:
        return None
    elif root.left is not None: #gdy ma lewe podrdrewo to poprzednikiem jest max w nim
        return getMax(node.left)
    else:
        p = node.parent
        while p is not None and node.key == p.left.key: #dopoki jest on lewym dzieckiem to ide w gore
            node = p
            p = p.parent
        return p


def sumOfNodes3(root):
    sum_ = 0
    while True:
        if root.left == None and root.right == None:
            sum_ += root.key
            return sum_

        elif root.left is None: #gdy nie ma lewego dziecka to dodaje do sumy wartosc roota i ide w prawo
            sum_ += root.key
            root = root.right

        elif root.left is not None: #gdy ma lewe dziecko
            c = root
            root = predecessor3(c,c.key) #szukam poprzednika lewego dziecka

            #gdy poprzednik jest wiekszy od elemntu dla którego go szukałam
            #tzn ze skorzystałam z krawędzi wracającej
            #to usuwam krawędź wsteczną(by naprawić drzewo), dodaje el do sumy i ide w prawe dziecko elementu
            if root.key > c.key: #gdy okaze sie ze wejde w krawędź powrotną
                root.right = None
                sum_ += c.key
                root = c.right
            else:
                root.right = c #prawe dziecko poprzednika wskazuje na moj el
                root = c.left #przechodze w lewo z moejgo elementu


root3 = BST_Node3(6)
insert3(root3,1)
insert3(root3,2)
insert3(root3,7)
insert3(root3,4)
insert3(root3,8)
insert3(root3,9)
print(sumOfNodes3(root3))


A = BST_Node3(21)
insert3(A, 15)
insert3(A, 5)
insert3(A, 7)
insert3(A, 13)
insert3(A, 8)
insert3(A, 20)
insert3(A, 37)
insert3(A, 25)
insert3(A, 23)
insert3(A, 26)
insert3(A, 40)
print(sumOfNodes3(A))

