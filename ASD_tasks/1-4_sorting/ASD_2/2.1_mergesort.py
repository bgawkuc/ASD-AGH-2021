#funkcja sortujaca 2 posortowane listy jednokierunkowe
class Node():
    def __init__(self):
        self.next = None
        self.value = None

#tablice przerabiam na liste
def tab2list(T):
    L = Node()
    A = L
    for i in range(len(T)):
        B = Node()
        B.value = T[i]
        A.next = B
        A = B
    return L.next

def printList(L):
    while L:
        print(L.value, end=" ")
        L = L.next
    print("|")

#scal posortowae listy z wartownikami
def merge(L1,L2):
    L = Node()
    tail = L
    f1 = L1.next
    f2= L2.next
    while f1 and f2:
        if f1.value < f2.value:
            tail.next = f1
            f1 = f1.next
        else:
            tail.next = f2
            f2 = f2.next
        tail = tail.next
    if f1:
        tail.next = f1
    if f2:
        tail.next = f2
    return L

#scalanie na listach bez wartownikow
def merge0(L1,L2):
    head = Node()
    tail = head

    while L1 and L2:
        if L1.value < L2.value:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next

    if L1 is None:
        tail.next = L2
    if L2 is None:
        tail.next = L1
    while tail.next:
        tail = tail.next

    return head.next, tail

#dzieli liste na podciag niemalejacy zaczynajacy sie od poczatku
# i reszte, zwraca wskaznik na reszte
def cutList(L):

    while L is None:
        return None

    while L.next and L.next.value >= L.value:
        L = L.next

    H = L.next
    L.next = None
    return H,L

#mergesort uzywajac funkcji cutlist
def mergesort(L):
    while True:
        NH = None #nowa głowa
        NT = None #nowy ogon
        while True:

            if L == None:
                L = NH
                break

            A = L
            L,T = cutList(L)

            if NT == None and L == None: #gdy cala lista jest posortowana
                return A

            if L == None: #ostatni odcięty fragment ktory nie ma pary
                NT.next = A
                L = NH
                break

            # odcinam nowy fragment
            B = L
            L,_ = cutList(L)

            X,T = merge0(A,B)

            if NH == None:
                NH = X
            else:
                NT.next = X
            NT = T

#dziel i zwyciezaj
#dla linked_list z wartownikiem
#mergesort z uzyciem wyznaczania srodka
def mergesort1(L):
    first = L.next
    if first == None or first.next == None:
        return L
    curr = first
    mid = first
    while curr.next and curr.next.next:
         curr,mid = curr.next.next,mid.next
    next_mid = mid.next
    mid.next = None
    a = Node()
    # insert(a,next_mid)
    left = mergesort1(L)
    right = mergesort1(a)
    sorted_list = merge(left,right)
    return sorted_list



T = [3,1,2,6,1,7,1]
T1 = [1,4,5,7]
T2 = [2,3,6,8,9]
L1 = tab2list(T1)
L2 = tab2list(T2)
# printList(L1)
# printList(L2)
# L,t = merge(L1,L2)
# printList(L)
# printList(T)
L = tab2list(T)
printList(L)
printList(mergesort(L))
# H = cutList(L)
# printList(L)
# printList(H)








