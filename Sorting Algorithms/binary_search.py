# wyszukiwanie binarne
# w liście posortowanej rosnąco sprawdza czy znajduje sie element o wartości x
# złożoność: O(logn)

def binarySearch(A, l, r, x):
    if l <= r:
        mid = l + (r - l) // 2
        if A[mid] == x:
            return True
        elif x < A[mid]:
            return binarySearch(A, l, mid - 1, x)
        else:
            return binarySearch(A, mid + 1, r, x)
    return False
