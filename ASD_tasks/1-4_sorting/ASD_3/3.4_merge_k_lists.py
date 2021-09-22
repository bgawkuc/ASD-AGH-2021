#Proszę zaproponować algorytm scalający k posortowanych list.

#Wszystkie k linked list dodaje do kopca - min heap. Wyjmuje z kopca najmniejszy element, dodaje go do wyniku.
#Jesli linked lista była 1-elementowa to ją usuwam, w przecwinym wypadku przechodzę w niej dalej.
#Cała procedura powtarza się dopóki kopiec nie będzie pusty.

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def printList(L):
    while L:
        if L.next:
            print(L.value, end='->')
        else:
            print(L.value)
        L = L.next


def arr2list(A):
    L = Node()
    head = L
    for el in A:
        new = Node(el)
        L.next = new
        L = L.next
    return head.next


def leftChild(i):
    return 2 * i + 1


def rightVhild(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def heapifyMin(A, i):
    n = len(A)
    l = leftChild(i)
    r = rightVhild(i)
    mini = i

    if l < n and A[l].value < A[mini].value:
        mini = l
    if r < n and A[r].value < A[mini].value:
        mini = r

    if mini != i:
        A[i], A[mini] = A[mini], A[i]
        heapifyMin(A, mini)


def deleteMin(A):
    A[-1], A[0] = A[0], A[-1]
    A.pop()
    heapifyMin(A, 0)


def add2minHeap(A, el):
    A.append(el)
    n = len(A) - 1
    while parent(n) >= 0 and A[parent(n)].value > A[n].value:
        A[n], A[parent(n)] = A[parent(n)], A[n]
        n = parent(n)


def mergeKlists(L):
    heap = []

    # dodaje wszystkie listy do kopca
    for li in L:
        add2minHeap(heap, li)

    res = Node()
    head = res

    while heap:
        # lista o najmniejszym el
        mini = heap[0]
        minNode = mini

        # jak była 1-elementowa to ją usuwam
        if mini.next is None:
            deleteMin(heap)
        # jak miała więcej el to przechodze na niej o 1 element dalej
        else:
            heap[0] = heap[0].next
            heapifyMin(heap, 0)

        # najmniejszy element dodaje do wyniku
        minNode.next = None
        res.next = minNode
        res = res.next

    return head.next


t1 = [1, 2, 2, 3, 8, 11]
t2 = [4, 5, 5, 6, 7]
t3 = [6, 7, 8, 12, 14]
l1 = arr2list(t1)
l2 = arr2list(t2)
l3 = arr2list(t3)
T = [l1, l2, l3]

L = mergeKlists(T)
printList(L)

