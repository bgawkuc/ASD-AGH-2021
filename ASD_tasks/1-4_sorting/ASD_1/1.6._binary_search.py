Proszę zaimplementować funkcję, która otrzymuje na wejściu posortowaną niemalejąco tablicę A o rozmiarze n oraz
liczbę x i sprawdza, czy x występuje w A. Jeśli tak, to zwraca najmniejszy indeks, pod którym x występuje.

def binarySearch(A,l,r,x):
    if i <= j:
        mid = l + (r-l) // 2
        if A[mid] == x:
            res = binarySearch(A,l,mid-1,x)
            if res == None:
                return mid
            return res
        elif A[mid] > x:
            return binarySearch(A,l,mid-1,x)
        else:
            return binarySearch(A,mid+1,r,x)
