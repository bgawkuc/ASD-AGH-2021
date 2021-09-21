#quicksort
#zlożoność: O(nlogn)

#jako pivot przyjmuje element mający indeks r
#przenosi na lewo od niego wszystkie elemnty mniejsze
def partition(A,l,r):
    piv = A[r]
    i = l

    for j in range(l,r):
        if A[j] <= piv: 
            A[j], A[i] = A[i], A[j] 
            i += 1

    A[i], A[r] = A[r], A[i] t
    return i

def quicksort(A,l,r):
    #rekurenycjne wywołanie dla list rozmiaru minimum 2
    if l < r:
        piv = partition(A,l,r)
        quicksort(A,l,piv-1)
        quicksort(A,piv+1,r)
    return A
