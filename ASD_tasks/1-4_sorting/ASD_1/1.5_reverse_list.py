#Proszę zaimplementować funkcję odwracającą listę jednokierunkową

class Node:
    def __init__(self):
        self.next = None
        self.value = None

def rev(L):
    prev = None
    curr = L
    while curr:
        #ustawiam na kolejny node, przepinam wskaźniki i aktualizuje obecny node
        after = curr.next 
        curr.next = prev 
        prev = curr 
        curr = after 
    return prev
