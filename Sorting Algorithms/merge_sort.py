#sortowanie przez scalanie
#złożoność: O(nlogn)


def mergeSort(A):
    if len(A) > 1:
        #indeks środka listy
        mid = len(A) // 2 

        #wywołanie rekurenycjne dla listy A podzielonej na pół
        L = A[:mid] #(od 0-mid-1)
        R = A[mid:] #(mid-końca)

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        #scalanie 2 list: L i R
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
            
    return A
