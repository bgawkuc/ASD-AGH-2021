#sortowanie przez kopcowanie
#złożonośc: O(nlogn)

def heapifyMax(A,i,n): 
    l = 2*i+1 
    r = 2*i+2 
    maxi = i 

    #szukam najwiekszej wartosci dla indeksow l,r,maxi(rodzic)
    if l < n and A[l] > A[maxi]:
        maxi = l
    if r < n and A[r] > A[maxi]:
        maxi = r
    
    #jeśli dziecko miało większą wartość niż rodzic
    if maxi != i:
        A[i], A[maxi] = A[maxi], A[i]
        heapifyMax(A,maxi,n)

#buduje kopiec na bazie listy A
def bulitHeap(A):
    n = len(A)
    for i in range(n-1,-1,-1):
        heapifyMax(A,i,n)
    return A

#sortuje liste wejściową
def heapSort(A):
    n = len(A)
    bulitHeap(A)
    for i in range(n-1,0,-1):
        A[i], A[0] = A[0], A[i]
        heapifyMax(A,0,i) #i = 0; n = i
    return A
