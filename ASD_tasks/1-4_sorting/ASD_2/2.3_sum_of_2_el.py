#Dana jest posortowana tablica A[1...n] oraz liczba x. Proszę napisać program,
# który stwierdza czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x


def exist(T,x,l,r):
    if l < r:
        if T[l] + T[r] == x:
            return l,r,True
        if T[l] + T[r] < x:
            return exist(T,x,l+1,r)
        elif T[l] + T[r] > x:
            return exist(T,x,l,r)
    return False

def main(T,x):
    r = len(T) - 1
    return exist(T,x,0,r)

T = [1,3,5,7,9]

print(main(T,12))