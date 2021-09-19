#sortowanie przez zliczanie
#O(n+k)
#zlozonosc potencjalnie liniowa dla k <= n; gdzie k jest maksymalnym elementem w tablicy
#dziala gdy liczby w tablicy sa >= 0

#tworze tablice cnt rozmiaru o 1 wiekszym niz k
#przechodze liniowo po tablicy i zwiekszam o 1 cnt[A[i]]
#czyli zliczam ilosc wysatpien kazdej liczby
#przechodze po wszystkich tablicach
#dodajac do cnt[i] wartosc cnt[i-1]
#czyli zliczam ile jest mniejszych elementow przed nią
#przechodze liniowo po tablicy wejsciowej OD TYŁU
#zmniejszam cnt[A[i]] o jeden
#na polu output[cnt[A[i]]] ustawiam A[i]
#i dostaje posortowaną tablice - output


def countingSort(A):
    n = len(A)
    k = max(A)
    cnt = [0] * (k+1)
    output = [0] * n

    for i in range(n):
        cnt[A[i]] += 1

    for i in range(1,k+1):
        cnt[i] += cnt[i-1]

    #counting więc nie od tyłu
    for i in range(n):
        cnt[A[i]] -= 1
        output[cnt[A[i]]] = A[i]

    return output

A = [8,0,2,5,7,1,0,2,9]
print(countingSort(A))