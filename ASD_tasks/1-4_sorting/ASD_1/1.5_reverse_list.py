#Proszę zaimplementować funkcję odwracającą listę jednokierunkową

class Node:
    def __init__(self):
        self.next = None
        self.value = None

def rev(L):
    prev = None
    curr = L
    while curr:
        after = curr.next #ustawiam na 1 el za curr
        curr.next = prev #curr zaczyna wskazywac na prev
        prev = curr #przenosze prev o 1 w prawu
        curr = after #przenosze curr o 1 w prawo
    return prev


def print_List(L):
    if L is not None:
        print(L.value,end=" ")
        print_List(L.next)
    else:
        print()

L = Node()
n1 = Node()
n1.value = 6
L.next = n1
n2 = Node()
n2.value = 2
n1.next = n2
n3 = Node()
n3.value = 4
n2.next = n3
n4 = Node()
n4.value = 1
n3.next = n4
print_List(L)
print_List(rev(L))