#Proszę zaimplementować funkcję wstawiającą dowolny element do kopca binarnego (max heap).

#złożoność: O(logn)

def parent(i):
    return (i - 1) // 2


def add_to_heap(A, el):
    A.append(el)
    i = len(A) - 1
    while parent(i) >= 0 and A[i] > A[parent(i)]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)
