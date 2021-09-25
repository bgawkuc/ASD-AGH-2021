#dla zadanej pary x,y mam znalezc lca
#lca-lowest common ancestor
#najmniejszy wspolny przodek
#czyli taka wartosc ktora jest zarowno przodkiem x jak i y
#tylko ten prozdek musi byc jak najglebiej zakorzeniony

#poruszam sie od roota w drzewie
#jako przodka na poczatku ustawiam roota
#dopoki oba nody sa mniejsze/wieksze schodze w doł
#w momencie gdy juz nie spalniaja tego warunku:
#to obecny root zwracam jako przodek

#dziala to poniewaz aby jakis el byl przodkiem musi znajdowac sie wyzej
#najgłebszy przodek dla x, y to
#  przodek
#  /     \
# x       y
#wiec bede schodzic w dol dopoki x,y(OBA) bylyby mniejszej/wieksze od przodka
#a gdy dojde do tego przodka to jeden jest wiekszy, drugi mniejszy wiec moge go zwrocic

class BST_Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def insert(root,key):
    prev = None
    while root is not None:
        if key > root.key:
            prev = root
            root = root.right
        else:
            prev = root
            root = root.left

    if key < prev.key:
        prev.left = BST_Node(key)
        prev.left.parent = prev
    else:
        prev.right = BST_Node(key)
        prev.right.parent = prev


def longestCommonAncestor(root,x,y):
    while True:
        #oba mniejsze
        if x < root.key and y < root.key:
            root = root.left

        #oba większe
        elif x > root.key and y > root.key:
            root = root.right

        else:
            return root.key

root = BST_Node(15)
insert(root,10)
insert(root,25)
insert(root,20)
insert(root,30)
insert(root,18)
insert(root,22)
insert(root,12)
insert(root,8)
insert(root,6)
insert(root,9)

print(longestCommonAncestor(root,6,9))
