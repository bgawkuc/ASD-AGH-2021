# Dane są następujące struktury:
# struct Node { Node* next; int val; };
# struct TwoLists { Node* even; Node* odd; };
# Napisać funkcję: TwoLists split(Node* list);
# Funkcja rozdziela listę na dwie: jedną zawierającą liczby parzyste i drugą zawierającą liczby
# nieparzyste. Listy nie zawierają wartowników.


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


def arr2list(A):
    n = len(A)
    L = Node()
    head = L
    for i in range(n):
        new = Node()
        new.value = A[i]
        L.next = new
        L = L.next
    return head.next


def twoLists(L):
    evenL = Node()
    oddL = Node()
    headE = evenL
    headO = oddL

    while L:
        node = L
        L = L.next
        node.next = None

        if node.value % 2 == 0:
            evenL.next = node
            evenL = evenL.next
        else:
            oddL.next = node
            oddL = oddL.next

    return headE.next, headO.next


A = [1, 3, 2, 9, 0, 4, 7, 2, 5]
L = arr2list(A)
printList(L)
print()
e, o = twoLists(L)
printList(e)
printList(o)
