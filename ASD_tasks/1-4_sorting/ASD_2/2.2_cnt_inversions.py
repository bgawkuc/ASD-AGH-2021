#Proszę zaproponować i zaimplementować algorytm, który mając na wejściu tablicę A zwraca
#liczbę jej inwersji (t.j., liczbę par indeksów i < j takich, że A[i] > A[j].

#lepszy zapis
#robie typowy mergesort, ale gdy lewy el jest wiekszy od prawego
#to zwiekszam licznik o tyle co wynosi dlg lewej tablicy-obecny idx w lewej tablicy
def func(A):
    cnt = 0

    def cntInversion(A):
        if len(A) > 1:
            #licznik inwersji
            nonlocal cnt
            mid = len(A) // 2

            L = A[:mid]
            R = A[mid:]

            cntInversion(L)
            cntInversion(R)

            l = r = a = 0
            print(L,R,cnt)
            while l < len(L) and r < len(R):
                #gdy po lewej el jest wiekszy od tego po prawej
                #to zwiekszam ilosc inwersji
                if L[l] > R[r]:
                    #len(L)-l czyli ilosc elementow jaka została w tablicy L
                    #one muszą byc na pewno mniejsze od R[r]
                    #bo wartosci w L są mniejsze od R
                    cnt += len(L)-l
                    A[a] = R[r]
                    r += 1
                else:
                    A[a] = L[l]
                    l += 1
                a += 1

            while l < len(L):
                A[a] = L[l]
                l += 1
                a += 1

            while r < len(R):
                cnt += len(L)-l
                A[a] = R[r]
                r += 1
                a += 1

    cntInversion(A)
    return cnt

#8
T = [5,2,4,0,1]
#10
A = [1,2,3,4,0,5,6,0]
print(func(T))

#robie typowego mergsorta ale przy okazji zliczam inwersje w mniejszych podtablicach
#jesli w lewej podtablicy el beda wieksze od tych w prawej tzn to inwersja
def merge(T,l,m,r):
    inver = 0
    T1 = [None] * (r-l+1)
    i = l
    j = m+1
    t = 0

    while i <= m and j <= r:
        if T[i] <= T[j]:
            T1[t] = T[i]
            i += 1
        else: #gdy el z < ind jest > wartoscia
            inver += m + 1 - i #od ilu el z lewej str jest on wiekszy
            T1[t] = T[j]
            j += 1
        t += 1

    while i <= m: #gdy zostala mi koncowka lewej tab
        T1[t] = T[i]
        i += 1
        t += 1
    while j <= r: #gdy zostala mi kocowka prawej tab
        inver += m + 1 - i
        T1[t] = T[j]
        j += 1
        t += 1

    #dopisuje posortowane el do starej tab na odpowiednie miejsca
    t = 0
    for i in range(l,r+1):
        T[i] = T1[t]
        t += 1
    print(T)
    return inver

def mergesort(T,l,r):
    inver = 0
    if l < r:
        m = (l+r) // 2
        inver += mergesort(T,l,m)
        inver += mergesort(T,m+1,r)
        inver += merge(T,l,m,r)
    return inver

T = [5,2,4,0,1]
print(mergesort(T,0,len(T)-1))