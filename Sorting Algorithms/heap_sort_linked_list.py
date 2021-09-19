#podane operacje dotyczą min heap
#analogicznie da sie stworzyc maxheap
#tworze kopiec jako deque(bo operacje pop/popleft sa O(1))
#i dodaje wszystkie nody do tego
#jak robie minheap dla kilkulistto tworze tablice z kolejkami

#LINKED LISTA BEZ WARTOWNIKA

from collections import deque

class Node:
    def __init__(self):
        self.value = None
        self.next = None


def printList(L):
    while L:
        if L.next:
            print(L.value,end="->")
        else:
            print(L.value)
        L = L.next


def arrToList(A):
    L = None
    head = L
    for i in range(len(A)):
        if i == 0:
            L = Node()
            L.value = A[0]
            head = L
        else:
            L1 = Node()
            L1.value = A[i]
            L.next = L1
            L = L.next
    return head


def parent(i):
    return (i-1) // 2


def leftChild(i):
    return 2 * i + 1


def rightChild(i):
    return 2 * i + 2


def heapifyMin(A,i):
    n = len(A)
    l = leftChild(i)
    r = rightChild(i)
    mini = i

    if l < n and A[l].value < A[mini].value:
        mini = l
    if r < n and A[r].value < A[mini].value:
        mini = r

    if mini != i:
        A[i], A[mini] = A[mini], A[i]
        heapifyMin(A,mini)


def addToMinHeap(A,el):
    A.append(el)
    i = len(A) - 1
    while i > 0 and A[parent(i)].value > A[i].value:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def deleteMin(A):
    A[0], A[-1] = A[-1], A[0]
    A.pop()
    heapifyMin(A,0)

#tworzy kopiec(min heap) poprzez operacje add to heap
#O(nlogn) bo liniowe przejscie i operacja addToMinHeap(O(logn))
def heap(L):
    H = deque() #kopiec w formie kolejki by miec operacje pop/popleft w O(1)

    #dodaje elementy do kopca
    while L:
        node = L
        L = L.next
        node.next = None
        addToMinHeap(H,node)

    for h in H:
        printList(h)

A = [9,0,3,7,1,8,3,2]

L = arrToList(A)
heap(L)
