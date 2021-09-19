class Node:
    def __init__(self):
        self.value = None
        self.next = None


#tablice zamienia w liste
def tab2list(A):
    L = Node()
    head = L
    for i in range(len(A)):
        L1 = Node()
        L1.value = A[i]
        L.next = L1
        L = L.next
    return head


def insert(L,node):
    head = L
    while L.next:
        L = L.next
    L.next = node
    return head


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
    sortedList = None
    L = L.next #pomija wartownika

    while L:
        after = L.next
        sortedList = sortInsert(sortedList,L)
        L = after

    return sortedList

A = [9,8,0,3,6,7,1,0,2]
L = tab2list(A)
printList(L)
L = insertionSort(L)
printList(L)