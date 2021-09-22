# Proszę zaimplementować:
# 1. Scalanie dwóch posortowanych list jednokierunkowych do jednej.
# 2. Algorytm sortowania list jednokierunkowych przez scalanie serii naturalnych.

class Node():
    def __init__(self):
        self.next = None
        self.value = None

#scala 2 posortowane listy w jedną
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
    
    #tworzy nową listę R która zaczyna się po środkowym elemencie
    R = Node()
    R.next = mid.next
    R = R.next
    mid.next = None

    left = mergesort2(L)
    right = mergesort2(R)

    return merge2lists(left,right)        
