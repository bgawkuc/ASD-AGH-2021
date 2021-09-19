#sortowanie przez scalanie na listach

#wywołuje rekurencyjnie funkcje mergesort:
#jesli zostala 1 elementowa lub pusta lista to ją zwraca
#jesli nie to szukam w niej srodkowego noda
#wobec niego dzielę liste na dwie częsci
#lewą - od początku do srodkowego
#prawą - od elmentu po srodkowym do konca
#wywoluje rekurenycjnie mergesort dla lewej i prawej czesci
#i zwracam scaloną (merge) lewą i prawą część


#IMPLEMENTACJA NA LISTACH BEZ WARTOWNIKA
class Node1:
    def __init__(self,value=None):
        self.value = value
        self.next = None

def arr2list(A):
    L = Node1(None)
    head = L
    for el in A:
        new = Node1(el)
        L.next = new
        L = L.next
    return head.next

def printList(L):
    while L:
        if L.next:
            print(L.value,end='->')
        else:
            print(L.value)
        L = L.next


def merge2lists(L1,L2):
    L = Node1()
    head = L

    while L1 and L2:
        if L1.value < L2.value:
            L.next = L1
            L1 = L1.next
        else:
            L.next = L2
            L2 = L2.next
        L = L.next

    while L1:
        L.next = L1
        L1 = L1.next
        L = L.next
    while L2:
        L.next = L2
        L2 = L2.next
        L = L.next

    return head.next


def mergesort2(L):
    #gdy mam listy 0 lub 1 elementowe
    if L is None or L.next is None:
        return L

    #szkam srodka listy wobec którego będę ją dzielić
    curr = L
    mid = L
    while curr.next and curr.next.next:
        curr,mid = curr.next.next, mid.next

    #tworze liste R,która zaczyna sie od mid.next, usuwam z niej wartownika
    R = Node1()
    R.next = mid.next
    R = R.next
    #ucinam, zeby lista L konczyla sie na mid
    mid.next = None

    left = mergesort2(L)
    right = mergesort2(R)

    return merge2lists(left,right)

A = [2,0,1,9,2,9,4,0,3]
L = arr2list(A)
printList(L)
L = mergesort2(L)
printList(L)


#IMPLEMENTACJA NA LISTACH Z WARTOWNIKIEM
class Node:
    def __init__(self):
        self.value = None
        self.next = None


def insert(L,node):
    head = L
    while L.next is not None:
        L = L.next
    L.next = node
    return head


def printList(L):
    while L is not None:
        if L.next is not None:
            print(L.value,end="->")
        else:
            print(L.value)
        L = L.next

#scalanie 2 posortowanych linked_list
def merge(L1,L2):
    L = Node() #nowa lista
    head = L
    L1, L2 = L1.next, L2.next #przechodze bo wartownik

    while L1 and L2: #dopoki mam jakie el porownywac

        if L1.value < L2.value: #jesli el z L1 jest mniejszy od el z L2
            L.next = L1 #to L1 przepinam do L
            L1 = L1.next #L1 przeskakuje o 1 dalej

        else:
            L.next = L2
            L2 = L2.next
        L = L.next

    #gdy zostaną mi el w L1 lub L2 to przepinam pozostałe
    if L1:
        L.next = L1

    if L2:
        L.next = L2

    return head


def mergeSort(L):
    if L.next is None or L.next.next is None: #dopoki nie bede miała 1 elementowcyh linked_list(L.next bo przeskakuje wartownika)
        return L

    #szukam srodka listy
    curr = L.next
    mid = L.next
    while curr.next and curr.next.next:
        curr, mid = curr.next.next, mid.next

    nextMid = mid.next #prawa polowa listy, tworze nową listę dla niej
    L1 = Node()
    insert(L1, nextMid)
    mid.next = None  # lewa połowa listy

    # rekurenycjnie dzielenie tablicy na mniejsze
    left = mergeSort(L)
    right = mergeSort(L1)

    return merge(left,right) #scalam lewą i prawą część


L = Node()
l = [2,4,2,6,8,3]


for i in range(len(l)):
    a = Node()
    a.value = l[i]
    insert(L,a)
# printList(L.next)

L = mergeSort(L)
# printList(L.next)

