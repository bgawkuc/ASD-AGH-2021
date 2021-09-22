#Dana jest posortowana tablica A[1...n] oraz liczba x. Proszę napisać program,
#który stwierdza czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x.

def exist(A,i,j,x):
    if i >= j:
        return False
    #gdy suma jest za duża zmniejsza prawy indeks
    if A[i] + A[j] > x:
        return exist(A,i,j-1,x)
    #gdy suma jest za mała zwiększa lewy indeks
    elif A[i] + A[j] < x: 
        return exist(A,i+1,j,x)
    else :
        return True


