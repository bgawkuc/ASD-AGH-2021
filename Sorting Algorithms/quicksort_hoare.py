#algorytm quicksort
#tylko procedura partition wygląda inaczej
#jako pivot ustawiam 1 element
#mam dwa wskazniki: lewy i prawy którymi się przesuwam po tablicy
#lewy przesuwam w prawo dopóki nie znajde elementu >= pivota
#prawy przesuwam w lewo dopoki nie znajde elementu <= pivota
#wtedy takie dwa elementy zamieniam miejscami
#procedura trwa do momentu gdy l i r sie nie spotkają

def partitionHoare(A,l,r):
    piv = A[l]
    i, j = l, r

    while True:
        while A[i] < piv:
            i += 1

        while A[j] > piv:
            j -= 1

        if i >= j:
            return j

        if i != j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1


def quickSort(A,l,r):
    if l < r:
        piv = partitionHoare(A,l,r)
        quickSort(A,l,piv)
        quickSort(A,piv+1,r)
    return A

A = [9,0,2,6,3,8,1]
print(quickSort(A,0,len(A)-1))