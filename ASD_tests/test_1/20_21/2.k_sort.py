# Węzły jednokierunkowej listy odsyłaczowej reprezentowane są w postaci:
# class Node:
# def __init__(self):
# self.val = None # przechowywana liczba rzeczywista
# self.next = None # odsyłacz do nastepnego elementu
# Niech p będzie wskaźnikiem na niepustą listę odsyłaczową zawierającą parami różne liczby rzeczywiste a1, a2, . . . , an (lista nie ma wartownika). Mówimy, że lista jest k-chaotyczna jeśli dla każdego elementu zachodzi, że po posortowaniu listy znalazłby się na pozycji różniącej się od bieżącej
# o najwyżej k. Tak więc 0-chaotyczna lista jest posortowana, przykładem 1-chaotycznej listy jest
# 1, 0, 3, 2, 4, 6, 5, a (n − 1)-chaotyczna lista długości n może zawierać liczby w dowolnej kolejności.
# Proszę zaimplementować funkcję SortH(p,k), która sortuje k-chaotyczną listę wskazywaną przez p.
# Funkcja powinna zwrócić wskazanie na posortowaną listę. Algorytm powinien być jak najszybszy
# oraz używać jak najmniej pamięci (w sensie asymptotycznym, mierzonym względem długości n
# listy oraz parametru k). Proszę oszacować jego złożoność czasową dla k = Θ(1), k = Θ(log n) oraz
# k = Θ(n).

class Node:
    def __init__(self):
        self.value = None
        self.next = None


def printList(L):
    while L:
        if L.next:
            print(L.value, end="->")
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
    return (i - 1) // 2


def leftChild(i):
    return 2 * i + 1


def rightChild(i):
    return 2 * i + 2


def heapifyMin(A, i):
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
        heapifyMin(A, mini)


def addToMinHeap(A, el):
    A.append(el)
    i = len(A) - 1
    while i > 0 and A[parent(i)].value > A[i].value:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def deleteMin(A):
    A[0], A[-1] = A[-1], A[0]
    A.pop()
    heapifyMin(A, 0)


from collections import deque


def kSort(L, k):
    H = deque()  # kopiec w formie kolejki by miec operacje pop/popleft w O(1)
    head = Node()
    result = head

    # dodaje k+1 elementow do kopca
    for _ in range(k + 1):
        node = L
        L = L.next
        node.next = None
        addToMinHeap(H, node)

    while len(H):
        mini = H[0]
        deleteMin(H)
        result.next = mini
        result = result.next

        if L:
            node = L
            L = L.next
            node.next = None
            addToMinHeap(H, node)

    return head.next


# k = 2
L2 = [2, 3, 5, 7, 11, 13, 17, 19, 31, 23, 29, 43, 41, 37, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
# k = 2
A = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]

L = arrToList(L2)
L1 = kSort(L, 2)
printList(L1)
