#Proszę zaimplementować funkcję, która mając na wejściu tablicę n elementów
#oblicza jednocześnie jej największy i najmniejszy element wykonując 1.5n porównań.

#sprawdzając elementy parami, mam mniej porównań
def minmax(A):
    mini = A[-1]
    maxi = A[-1]
    for i in range(0,len(A)-1,2):

        if A[i] < A[i+1]: 
            if A[i] < mini:
                mini = A[i]
            if A[i+1] > maxi:
                maxi = A[i+1]

        else:
            if A[i] > maxi:
                maxi = A[i]
            if T[i+1] < mini:
                mini = A[i+1]

    return mini,maxi
