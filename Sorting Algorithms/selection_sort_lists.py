#sortowanie przez wybieranie na listach
#zlozonosc O(n^2)

#biorę 1 element z listy - first
#ustawiam go jako minimalny - mini
#szukam po jego prawej stronie elementu mniejszego od niego
#po przejsciu listy zamieniam wartosciami: wartosc mini i wartosc first
#jako nowy first biore first.next
#dzieki temu sortuje liste, bo po kolei ustawiaja sie w niej najmniejsze elementy

class Node:
    def __init__(self):
        self.value = None
        self.next = None


#wstawianie node na koniec listy
#L-wskazanie na glowe
def insert(L,node):
    head = L
    while L.next is not None:
        L = L.next
    L.next = node
    return head


def printList(L):
    L = L.next
    while L is not None:
        if L.next is None:
            print(L.value)
        else:
            print(L.value,end="->")
        L = L.next
    print()


def selectionSort(L):
    first = L.next #1 el w liscie

    while first: #dopoki 1 el nie jest Nonem
        mini = first #1 element ustawiam na minimalny
        p = first.next

        #szukam czy po jego prawej znajdzie sie jakis mniejszy element
        while p:
            if p.value < mini.value:
                mini = p
            p = p.next
        #zamieniam wartością minimalny element i ten który był pierwszy
        mini.value, first.value = first.value, mini.value
        first = first.next #jako pierwszy biore kolejny z listy

    return L


L = Node()
T = [5,8,2,3,0,6,7,1]

for i in range(len(T)):
    node = Node()
    node.value = T[i]
    insert(L,node)
printList(L)

L = selectionSort(L)
printList(L)