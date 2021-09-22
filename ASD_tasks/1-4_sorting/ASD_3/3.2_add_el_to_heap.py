#Proszę zaimplementować funkcję wstawiającą dowolny element do kopca binarnego (max heap).

#kopiec jest reprezentowany jako lista
#dodaje element na koniec i naprawiam kopiec dopóki dziecko jest większe od rodzica
#złożoność: O(logn), n-rozmiar listy

def parent(i):
    return (i-1) // 2

def add_to_heap(A,el):
    A.append(el)
    i = len(A)-1
    while parent(i) >= 0 and A[i] > A[parent(i)]:
        A[i],A[parent(i)] = A[parent(i)],A[i]
        i = parent(i)
