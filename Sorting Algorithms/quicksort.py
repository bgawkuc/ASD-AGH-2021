#quicksort
#zlozonosc O(nlogn)

#WERSJA REKURENCYJNA
#wywoluje rekurencyjnie quicksort dopoki l < r; l,r-lewy/prawy idx przedzialu
#czyli dopoki mam przedziały minimum 2 elementowe
#szukam pivota za pomocą partition
#i wywoluje rekurencyjnie quicsort od l do pivota - 1 oraz od pivot + 1 do r

#WERSJA ITERACYJNA
#zuzywa jedynie O(logn) pamięci
#tworze stos S - pusta tablica, LIFO-last in first out
#wrzucam do niego pare: poczatek, koniec przedzialu
#dopoki stos nie jest pusty:
#zdejmuje pare l,r
#jesli l < r to wywoluje dla nich partition
#pivot dzieli tablice na 2 części: lewą i prawą
#jesli piv - l < piv - r (czyli lewa część jest mniejsza od prawej)
#to najpierw na stos wrzucam przedział wiekszy [piv+1,r] a potem mniejszy [l,piv-1]
#gdyby piv - l >= piv - r to najpierw wrzucam wiekszy [l,piv-1] a potem mniejszy [piv+1,r]
#stos dziala tak ze zdejmuje najpierw to co trafiło ostatnie - czyli zdejmuje zawsze mniejszy przedział
#stos w koncu bedzie pusty i wtedy tablica będzie posortowana

#PARTITION-SPOSÓB DZIAŁANIA
#partition-sortuje mi tablice wzgledem pivota
#czyli wszystko na lewo od pivota bedzie od niego mniejsze
#a wszystko na prawo od niego bedzie wieksze
#jako pivota wybieram ostatni element
#ustawiam i na wartosc l
#przechodze liniowo tablice
#jesli znaleziony element A[j] <= pivota
#to zamieniam miejscami A[i] oraz A[j], zwiekszam i o 1
#na samym koncu zamieniam miejscami A[i[ orz pivota


def partition(A,l,r):
    piv = A[r] #liczba wobec ktorej sortuje
    i = l

    for j in range(l,r):
        if A[j] <= piv: #jesli znajde el <= od pivota
            A[j], A[i] = A[i], A[j] #zamieniam z miejscem ten element z i
            i += 1

    A[i], A[r] = A[r], A[i] #na koncu zamieniam miejscami A[r] (pivot) i ostatnio zamieniony element
    return i

#rekurenycjny
def quicksort(A,l,r):
    if l < r:
        piv = partition(A,l,r)
        quicksort(A,l,piv-1)
        quicksort(A,piv+1,r)
    return A


#iteracyjny
#zuzywa jedynie O(logn) pamięci
def quicksortIter(A):
    n = len(A)
    l, r = 0, n-1
    S = [] #stos
    S.append((l,r))

    while S: #dopoki stos nie jest pusty
        l, r = S.pop()
        if l < r: #dopóki mam przedział max 2-elementowy o idx l < r
            piv = partition(A,l,r)

            # gdy prawa część jest większa
            #wrzucam prawy przedział(wiekszy) a potem lewy(mniejszy)
            if piv - l < r - piv:
                S.append((piv+1,r))
                S.append((l,piv-1))
            #wrzucam lewy przedział(większy) a potem prawy(mniejszy)
            else:
                S.append((l,piv-1))
                S.append((piv+1,r))

    return A


A = [2,9,0,3,7,1,9,3]
print(quicksort(A,0,len(A)-1))
print(quicksortIter(A))

