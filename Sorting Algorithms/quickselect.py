#quicksort w którym pivot jest wybierany losowao
#dla posortowanej - O(n^2), średnio - O(nlogn), optymistycznie - O(n)

#rozni sie tym ze pivot jest wybieramy losowo
#oraz w partition pivot trzeba wstawic na ostatnie miejsce(zamienic miejscami ostatni el i pivot)
#by była identyczna implementacja jak w quicksort

def partition(A,l,r):
    piv = A[r]
    i = l

    for j in range(l,r):
        if A[j] <= piv:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i

def quickselect(A,l,r):
    if l < r:
        piv = partition(A,l,r)
        quickselect(A,l,piv-1)
        quickselect(A,piv+1,r)
    return A

#gdy szukam jaka liczba bedzie pod k-tym indeksem w posortowanej tab
#randomiozwanie pivota psuje takie szuaknie
def k_index(A,l,r,k):
    if l <= r:
        q = partition(A,l,r)
        if q - l == k:
            return A[q]
        elif k < q - l:
            return k_index(A,l,q-1,k)
        else:
            return k_index(A,q+1,r,k-q-1+l)


A = [8,2,5,7,1,0]
for i in range(len(A)):
    A1 = A[:]
    print(k_index(A1,0,len(A1)-1,i))

# print(quickselect(A,0,len(A)-1))