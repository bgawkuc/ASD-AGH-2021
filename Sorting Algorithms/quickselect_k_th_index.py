#quickselect
#wykorzystywany do znalezeienia jaka wartosc znajdzie sie pod k-tym indeksem
#optymistyczna zlożoność O(n), pesymistyczna O(n^2)

#działa tak jak quickselect
#tylko nie sortuje całej tablicy do konca
#a jedynie część którą potzrebuje
#losowy pivot
#szukanie za pomocą mediany median lepsze

from random import randint

def pivot(l,r):
    return randint(l,r)


def partition(A,l,r):
    idx = pivot(l,r)
    A[idx], A[r] = A[r], A[idx]
    piv = A[r]
    i = l

    for j in range(l,r):
        if A[j] <= piv:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i


def k_th_idx(A,l,r,k):
    if l <= r:
        q = partition(A,l,r)
        if q - l == k:
            print(A)
            return A[q]
        elif k < q - l:
            return k_th_idx(A,l,q-1,k)
        else:
            return k_th_idx(A,q+1,r,k-q-1+l)

A = [2,0,1,8,2,6,3,5,0]
print(k_th_idx(A,0,len(A)-1,2))

print(sorted(A))