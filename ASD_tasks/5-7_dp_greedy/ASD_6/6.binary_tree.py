#mamy drzewo binarne(lisc ma max 2 dzieci)
#znajdz sciezke ktora ma najwieksza wartosc
#wierzcholki maja wart dod i ujemne

#do funkcji przekazuje wierzchołek drzewa
#findBestPath(v) to dlugosc najdlzuszej sciezki zakorzenionej w v
#oblicz ją rekurencyjnie
#dla v == 0 zwracam (0,0)
#oblicza rekurenycjnie bestL, L dla v.l
#oraz bestR, R dla v.r
#gdzie bestL,bestR to wartosc najlepszycg sciezek w drzewie zakorzenionych w DOWOLONYM wiercholku
#i ta sciezka moze wygląadc: lewe dzeicko, rodzic, prawe dziecko
#a L,R to wartosc najlepszych ścieżek wychodzacych z KONKRETNEGO wierzcholka
#a to są sciezki proste czyli nie biore pod uwage sytuacji lewe dziecko, rodzic, prawe dziecko
#potem liczę wartosc v.bestPath jako max z: 0, v.val, v.val + L, v.val + r
#a potem licze best jako max z bestL, bestR, v.bestPath, L+R+v.val
#i zwracam best, v.bestPath
#czyli wartosc najlepszej sciezki w drzewie i wartosc najlepszej sciezki dla v

#drzewo
#       -1
#      /   \
#    -2     16
#    / \    /
#   10  4  -8

#dla 10: L=0,R=0,bestL=0,bestR=0                v.bestPath = 10,best = 10
#dla  4: L=0,R=0,bestL=0,bestR=0                v.bestPath = 4,best = 10
#dla -2: L=8(10-2),R=2(4-2),bestL=10,bestR=4    v.bestPath = 8,best = 12(bo 10+4-2)
#dla -8: L=0,R=0,bestL=0,bestR=0                v.bestPath = 0,best = 12
#dla 16: L=0,R=0,bestL=0,bestR=0                v.bestPath = 16,best = 16
#dla -1: L=7,R=15,bestL=12,bestR=16             v.bestPath = 15,best = 23(16-1-2+10)
#wynik:23


class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.bestPath = 0


def findBestPath(v):
    if v == None:
        return (0,0)

    bestL, L = findBestPath(v.left)
    bestR, R = findBestPath(v.right)


    #dlg najlespzej sciezki zakorzenionej w v
    #biore sam lisc v, lisc v + sciezke na lewo, lisc v + sciezke na prawo lub 0
    v.bestPath = max(0,v.val,v.val+L,v.val+R)
    #best to ogolnie najlepsza sciezka w calym drzewie
    #biore max z sciezki dla x, najdluzszej sciezki w lewyej częsci lub w prawej
    #lub wartosc lewego poddrzewa rodzic i prawego poddrzewa(obrocone v)
    best = max(v.bestPath,bestL,bestR,L+R+v.val)

    return (best,v.bestPath)


v = Node(-1)
u = Node(-2)
w = Node(3)
z = Node(10)

v.left = u
v.right = w
w.left = z

a = Node(1)
b = Node(-2)
c = Node(16)
d = Node(10)
e = Node(4)
f = Node(-8)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

x = Node(1)
y = Node(-2)
m = Node(6)
z = Node(3)
x.left = y
x.right = z
y.left = m

withoutRoot, withRoot = findBestPath(v)
print(max(withRoot,withoutRoot))

