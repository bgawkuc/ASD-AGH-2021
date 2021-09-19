#counting sort na listach

#znajduje max wartosc w liscie
#takiego rozmiaru tworze L
#przechodze po L i zapisuje ilosc wystapien kazdej liczby
#ustawiam wartosc ja na 0
#przechodze poliscie
#jesli cnt dla obecnej wartosci wynosi 0 to j zwiekszam o 1
#a jak nie to zmieniam wartosc obecnego noda na j oraz zmniejszam ilosc cnt dla noda o 1

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


def maxValue(L):
    L = L.next
    maxi = L.value
    while L:
        if L.value > maxi:
            maxi = L.value
        L = L.next
    return maxi


def printList(L):
    L = L.next
    while L is not None:
        if L.next is None:
            print(L.value)
        else:
            print(L.value,end="->")
        L = L.next
    print()


def countingSort(L):
    maxi = maxValue(L)
    L1 = L
    cnt = [0] * (maxi+1)

    L = L.next
    while L:
        cnt[L.value] += 1
        L = L.next

    L = L1
    j = 0
    head = L
    L = L.next

    while L:
        if cnt[j] == 0:
            j += 1
        else:
            L.value = j
            cnt[j] -= 1
            L = L.next

    return head


A = [8,5,3,7,6,8,4]
L = tab2list(A)
printList(L)
printList(countingSort(L))