#sortowanie pozycyjne
#jest to zmodyfikowany counting sort
#który radzi sobie dobrze gdy w tablicy mam liczby kilkucyfrowe
#O(d*(n+k)); d-najwieksza ilosc cyfr w liczbie w tablicy, k-liczba roznych cyfr(zakres 0-9)
#potencjalnie liniowe o ile d oraz n nie będą podobne lub d będzie wieksze od n

#jest to d wywołań counting sorta
#d-najwieksza ilosc cyfr w liczbie
#wywołania są dla 1 cyfry, 2 cyfry, ..., d-tej cyfry licząc OD TYŁU
#sortuje w tablicy liczby wzgledej danej i-tej cyfry za pomocą counting sorta
#aktualizuje tablice
#i powtarzam to samo wzgledem kolejnej cyfry
#gdy jakas liczba nie posiada i-tej cyfry to traktuje jakby na tym miejscu było 0



def countingSort(A,l): #l-przez tyle bede dzielic moją liczbe (10^(0,1,2,...))
    n = len(A)
    cnt = [0] * 10 #mam tylko 10 cyfr
    output = [0] * n

    for i in range(n):
        j = (A[i] // l) % 10 #liczbe dziele na tyle co l( 10 ^jakiejs) i biore 1 cyfre w tej liczbie
        cnt[j] += 1

    for i in range(1,10):
        cnt[i] += cnt[i-1]

    #radix wiec od tyłu
    for i in range(n-1,-1,-1):
        j = (A[i] // l) % 10
        cnt[j] -= 1
        output[cnt[j]] = A[i]

    A[:] = output


def radixSort(A):
    l = 1
    while max(A) // l > 0:
        countingSort(A,l)
        l *= 10
    return A

A = [67,9028,870,1030,156,100,17,9,190,1982]
print(radixSort(A))