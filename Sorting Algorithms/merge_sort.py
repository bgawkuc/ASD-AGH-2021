#sortowanie przez scalanie
#O(nlogn)

#mam na wejsciu tablice wejsciową A
#dziele ją na połówki dopoki dlugosc tak podzielonej tablicy nie bedzie 1
#wtedy uruchamia sie scalanie
#bierze one tablice L oraz R i je łączy z zachowaniem kolejnosci rosnąco
#mniejsze tablice łączy w wieksze i tak do końca

#A = [6,2,3,7,0,1,5,4]
#[6] i [2] -> [2,6]
#[3] i [7] -> [3,7]
#[2,6] i [3,7] -> [2,3,6,7]
#[0] i [1] -> [0,1]
#[5] i [4] -> [4,5]
#[0,1] i [4,5] -> [0,1,4,5]
#[2,3,6,7] i [0,1,4,5] -> [0,1,2,3,4,5,6,7]


def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2 #środek tablicy

        #środek dzieli na 2 pojedyńcze
        L = A[:mid] #(od 0-mid-1)
        R = A[mid:] #(mid-końca)

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        #scalanie 2 tablic L i R
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


A = [6,2,3,7,0,1,5,4]
print(mergeSort(A))