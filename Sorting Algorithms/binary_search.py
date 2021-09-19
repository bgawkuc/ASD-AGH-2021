#wyszukiwanie binarne(połówkowe)
#O(logn)
#w posortowanej tablicy rosnąco sprawdza czy znajduje sie element x

#l,r-poczatek/koniec zakresu w którym sprawdzam
#wyznaczam srodek zakresu jesli x jest rowny wartosci ze srodka to zwracam True
#jesli x < wartosci dla srodka to r zmianiem na srodek - 1
#jesli x > wartosci srodka to l zmieniam na srodek + 1
#cala procedura powtarza sie dopoki l <= r
#gdy nie znajdzie takiej liczby zwraca false

#wersja rekurencyjna
def binarySearch(A,l,r,x):
    if l <= r:
        mid = l + (r - l) // 2
        if A[mid] == x:
            return True
        elif x < A[mid]:
            return binarySearch(A,l,mid-1,x)
        else:
            return binarySearch(A,mid+1,r,x)
    return False


#wersja iteracyjna
def binarySearchIter(A,x):
    l, r = 0, len(A) - 1
    while l <= r:
        mid = (l+r) // 2
        if A[mid] == x:
            return True
        elif x < A[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return False

A = [1,2,3,5,6,7,9]

print(binarySearchIter(A,4))