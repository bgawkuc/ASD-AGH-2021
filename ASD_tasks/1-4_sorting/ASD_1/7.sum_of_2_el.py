#Dana jest posortowana tablica A[1...n] oraz liczba x. Proszę napisać program,
#który stwierdza czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x.

def exist(A, i, j, x):
    if i >= j:
        return False
    if A[i] + A[j] > x:
        return exist(A, i, j - 1, x)
    elif A[i] + A[j] < x:
        return exist(A, i + 1, j, x)
    else:
        return True
