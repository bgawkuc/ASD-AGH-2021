#sortowanie kubełkowe na listach

#pisze funkcje które wyznaczaja mi wartosc max element oraz ilosc elementow liscie
#tworze tyle kubełków co rozmiar listy
#kazdy na poczatku jest jako None
#przechodze po liście
#wyjmuje noda, liste ustawiam na L.next
#odcinam końcowke node, na podstawie jego wartosci okreslam do jakiego kubełka ma trafic
#idx kubełka to : int( ( (node.value-mini) / ((maxi-mini) * (n)) ) lub int( ( (node.value-mini) / ((maxi-mini) * (n)) ) - 1
#drugi wzór zachodzi jedynie dla wartości max w tablicy
#jesli ten kubełek jest pusty to ten element staje sie jego głową
#a jesli nie to go dodaje do listy tego kubełka
#przechodze liniowo po kubełkach, jeśli kubełek nie jest pusty
#sortuje go i dodaje do listy wynikowej


class Node:
    def __init__(self):
        self.value = None
        self.next = None


def insert(L,node):
    head = L
    while L.next:
        L = L.next
    L.next = node
    return head


def tab2list(A):
    L = Node()
    head = L
    for i in range(len(A)):
        L1 = Node()
        L1.value = A[i]
        L.next = L1
        L = L.next
    return head


def maxValue(L):
    L = L.next
    maxi = L.value
    while L:
        if L.value > maxi:
            maxi = L.value
        L = L.next
    return maxi


def minValue(L):
    L = L.next
    mini = L.value
    while L:
        if L.value < mini:
            mini = L.value
        L = L.next
    return mini


def sizeList(L):
    n = 0
    L = L.next
    while L:
        n += 1
        L = L.next
    return n


def printList(L):
    # L = L.next
    while L is not None:
        if L.next is None:
            print(L.value)
        else:
            print(L.value,end="->")
        L = L.next
    print()


def sortInsert(L,el):
    #gdy wstawiam el na poczatek
    if not L or el.value <= L.value:
        el.next = L
        return el

    curr = L
    while curr.next and curr.next.value < el.value:
        curr = curr.next

    el.next = curr.next
    curr.next = el
    return L


def insertionSort(L):
    #nowa lista
    sortedList = None
    L = L.next

    #przechodze po L, urywam po 1 nodzie i wstawiam go w odpowiednie miejsce do sortedlist
    while L:
        after = L.next
        sortedList = sortInsert(sortedList,L)
        L = after
    return sortedList


def bucketSort(L):
    n = sizeList(L)
    maxi = maxValue(L)
    mini = minValue(L)
    r = (maxi - mini) / n
    buckets = [None for _ in range(n)]
    L = L.next

    while L:
        node = L
        L = L.next
        node.next = None

        d = (node.value - mini) / r - int((node.value - mini) / r)

        if d == 0 and node.value != mini:
            bucketIdx = int((node.value - mini) / r) - 1
        else:
            bucketIdx = int((node.value - mini) / r)

        # num = (node.value - mini) / (maxi-mini)
        # buketIdx = int(num * (n-1))

        if buckets[bucketIdx] is None: #gdy kubelek jest pusty
            head = Node()
            head.next = node
            buckets[bucketIdx] = head
        else: #gdy kubełek nie jest pusty
            insert(buckets[bucketIdx],node)

    result = Node()
    head = result

    for bucket in buckets:
        if bucket:
            bucket = insertionSort(bucket)
            insert(result,bucket)
    return head


A = [6,8,9,2,0,8]
L = tab2list(A)
L = (bucketSort(L))
printList(L)