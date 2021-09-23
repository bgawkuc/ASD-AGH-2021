#Dostajesz na wejściu tablice A[n] i wartość k. Wartość pola A[i] wynosi 0 lub 1.
#1 oznacza, że istnieje możliwość wybudowania maszyny w danym miejscu.
#Jeśli maszynę wybudowano w i-tym miejscu to chroni ona: abs(i-j) < k.
#Znajdź miejsca gdzie należy wybudować maszyny, by ich ilość była minimalna i każde miejsce w A było chronione.
#Jeśli nie istnieje taki wybór punktów zwróć False.

def machines(A,k):
    n = len(A)

    #szukam miejsca dla 1 maszyny (o jak najdalszym indeksie)
    first = None
    for i in range(k-1,-1,-1):
        if A[i] == 1:
            first = i
            break
    #gdy nie wszystkie miejsca byłyby chronione
    if first is None:
        return False
    mach = [first]

    #do jakiego indeksu do przodu mam chronione miejsca
    protected = first + k - 1

    #dopoki nie wszystkie pola są chronione
    while protected < n-1:

        new = None
        #szukam jak najdalszego miejsca na nową maszyne
        for i in range(protected+k-1,protected,-1):
            if i < n and A[i] == 1:
                new = i
                mach.append(i)
                break

        #jesli nie ma takiego miejsca
        if new is None:
            return False
        else:
            protected = new + k - 1

    return mach
