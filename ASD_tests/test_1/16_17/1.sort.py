# Dana jestr struktura opisująca listę jednokierunkową dla liczb rzeczywistych:
# struct Node{ Node* next; double value; }
# Proszę zaimplementować funkcję void Sort( Node* list ), która otrzymuje na wejściu listę
# liczb rzeczywistych (z wartownikiem), wygenerowaną zgodnie z rozkładem jednostajnym na
# przedziale [0,10) i sortuje jej zawartość w kolejności niemalejącej. Funkcja powinna być możliwie
# jak najszybsza (biorąc pod uwagę warunki zadania). Proszę oszacować złożoność
# zaimplementowanej funkcji.


class Node():
    def __init__(self):
        self.next = None
        self.value = None


def printList(L):
    while L:
        print(L.value, end=" ")
        L = L.next
    print()


def tab2list(T):
    L = Node()
    A = L
    for i in range(len(T)):
        B = Node()
        B.value = T[i]
        A.next = B
        A = B
    return L.next


def length(L):
    cnt = 0
    while L:
        L = L.next
        cnt += 1
    return cnt


def max_minValue(L):
    maxi = L.value
    mini = L.value
    L = L.next
    while L:
        if L.value > maxi:
            maxi = L.value
        if L.value < mini:
            mini = L.value
        L = L.next
    return mini, maxi


def appendToList(L, el):
    head = L
    while L.next:
        L = L.next
    L.next = el
    return head


def sortedInsert(L, el):
    if not L or L.value >= el.value:
        el.next = L
        L = el
    else:
        curr = L
        while curr.next and el.value > curr.next.value:
            curr = curr.next

        el.next = curr.next
        curr.next = el
    return L


def insertionSort(L):
    sorted = None
    curr = L

    while curr:
        after = curr.next
        sorted = sortedInsert(sorted, curr)

        curr = after

    L = sorted
    return L


def bucket_sort(L):
    n = length(L)
    mini, maxi = max_minValue(L)
    rang = (maxi - mini) / n

    buckets = [None for _ in range(n)]

    while L:
        diff = ((L.value - mini) / rang) - int((L.value - mini) / rang)

        if diff == 0 and L.value != mini:
            ind = (int((L.value - mini) / rang)) - 1
        else:
            ind = (int((L.value - mini) / rang))

        new = L.next
        L.next = None

        if buckets[ind] is None:
            A = Node()
            A.value = L.value
            buckets[ind] = A
        else:
            appendToList(buckets[ind], L)

        L = new
    res = Node()
    r = res

    for b in buckets:
        if b is not None:
            b = insertionSort(b)
            appendToList(r, b)

    return res.next


t = [9, 8, 2, 1, 0, 5, 8, 7, 1]
L = tab2list(t)
printList(L)
x = bucket_sort(L)
printList(x)
