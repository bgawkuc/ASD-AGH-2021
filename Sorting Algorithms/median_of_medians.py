#mediana median/magiczne piątki
#wykorzystywana często by podac liczbe ktora bedzie miala k-ty indeks w posortowanej tab
#zwraca wartosc mediany median/moze tez zwracac idx

#dzielimy tab na podtablice 5 elementowe ktore sortujemy(dowolne sortowanie)
#ostatnia tablica moze nie byc 5-elementowa, zalezy to od rozmiaru wejsciowej tablicy
#z kazdej takiej tablicy wybieramy srodkowy element(mediane)
#dla parzystych rozmiarów tablicy będzie to srodkowy-lewy element
#tworzymy tablice z medianami
#gdy rozmiar tablicy z medianami bedzie <= 5 to zwracam mediane jako srodkowy element tablicy z medianami
#a jak nie to rekurenycjnie szukam mediany w ten sam sposób
#zlozonosc liniowa O(n)

#sortowanie podtablic
def insertionSort(A, l, r):
    for i in range(l + 1, r + 1):
        el = A[i]
        j = i - 1
        while j >= l and A[j] > el:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = el
    return A


def median(A, l, n):
    r = l + n - 1
    insertionSort(A, l, r) #sortuje przedział
    return l + (n - 1) // 2 #zwraca srodkowy el przedzialu-mediane


def medianOfMedians(A, l, r): #l,r-idx lewego i prawego brzegu przedziału
    n = r - l + 1

    #cntMed - ilosc median dla przedziału od A[l] do A[r]
    if n % 5 == 0:
        cntMed = n // 5
    else:
        cntMed = n // 5 + 1


    #dzielenie tablicy na piątki i szukanie w nich mediany
    #mediany wrzucam na poczatek tablicy wejsciowej
    i = l
    while i * 5 + 4 < n:
        m = median(A, i * 5, 5)
        A[m], A[i] = A[i], A[m]
        i += 1

    #ostatnia tablica, która moze miec mniez niz 5 elementow
    if i * 5 < n:
        m = median(A, i * 5, n % 5)
        A[m], A[i] = A[i], A[m]

    #sprawdzam ile median mam, jesli < 6 to sie da wyznaczyc juz mediane
    #a jak nie to rekurenycyjnie odpalam algorytm
    if cntMed == 1:
        return A[0]
    elif cntMed < 6:
        return A[median(A, l, cntMed)]
    else:
        return medianOfMedians(A, l, l + cntMed - 1)


from random import randint
t = [randint(1,10) for _ in range(17)]
print(t)
print(medianOfMedians(t,0,len(t) - 1))


#
