#mam ciąg przedziałów domkniętych [a1, b1], . . . ,[an, bn].
#podaj algorytm, który znajduje taki przedział [at, bt], w którym w całości
#zawiera się jak najwięcej innych przedziałów.

# mam tablice przedzialów+inf jaki ma on idx w startowej
# sortuje tą tablice po początkach i po koncach
# dla danego przedziału zapisuje ile przedziałow ma mniejszy x od niego i ile ma mniejszy y
# y-x to ilosc przedziałow ktore sie w nim zawiera, gdy y-x <= 0-zaden sie nie zawiera
# szukam przedziały dla którego y -x jest największa


#CZYTELNIEJSZY
def partition(A, l, r, k):
    pivot = A[r][k]
    i = l
    for j in range(l, r):
        if A[j][k] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i


# k-po jakim idx sortuje
def quicksort(A, l, r, k):
    if l < r:
        q = partition(A, l, r, k)
        quicksort(A, l, q - 1, k)
        quicksort(A, q + 1, r, k)
    return A


def func(A):
    n = len(A)
    # dodaje inf o idx w tablicy A
    for i in range(n):
        A[i].append(i)

    # startX,endY-tablica z przedzialami posortowana po poczatkach,po koncach rosnąco
    startX = quicksort(A[:], 0, n - 1, 0)
    endY = quicksort(A[:], 0, n - 1, 1)

    # x,y-pod odpowiednimi indeksami(0 do n-1) znajduje sie ilosc przedzialow jaka ma wiekszy x/mniejszy y
    x = [0] * n
    y = [0] * n

    # wypelniam tablice x,y
    for i in range(n):
        #który z kolei (w posortowanej po początkach tablicy)
        #jest przedział który w wejsciowej tablicy miał indeks startX[i][2]
        x[startX[i][2]] = i
        # który z kolei (w posortowanej po końcach tablicy)
        # jest przedział który w wejsciowej tablicy miał indeks endY[i][2]
        y[endY[i][2]] = i

    # diff-roznica y-x dla odpowiendiego idx czyli ilosc przedzialow jakie sie zawiera w i-tym
    diff = [0] * n

    maxi = -float("inf")
    maxiIdx = float('inf')

    #wypełniam tablice diff, szukam idx dla którego mam najwiecej zawierających się przedziałów
    for i in range(n):
        diff[i] = y[i] - x[i]
        if diff[i] > maxi:
            maxiIdx = i
            maxi = diff[i]

    # zwraca przedział który ma najwiekszą wartosc diff-najwiecej sie w nim zawiera
    return A[maxiIdx][:2]


t = [[6, 7], [3, 5], [1, 6], [2, 7]]
print(func(t))


#TO SAMO ALE MNIEJ CZYTELNY KOD

#dla kazdego przedzialu zliczam ile x jest <= od mojego x
#ile y jest <= od mojego y
#y - x = to ilosc ile sie w nim zawiera
#szukam potem najwiekszego y - x
#jesli y - x <= 0 tzn ze 0
#zlozonosc sortowania O(nlogn)
#zloznoscs petli w funkcji O(n)
#czyli sumaryczna zlonosc to O(n+nlogn) -->  O(nlogn)

def partition2(T,l,r,k):
    pivot = T[r][k]
    i = l - 1
    for j in range(l,r):
        if T[j][k] <= pivot:
            i += 1
            T[i],T[j] = T[j],T[i]
    T[r],T[i+1] = T[i+1],T[r]
    return i+1

#T - tablica przedziałów
#k-na idx jakiego elementu patrze
def Quicksort(T,l,r,k):
    if l < r:
        q = partition2(T,l,r,k)
        Quicksort(T,l,q-1,k)
        Quicksort(T,q+1,r,k)
    return T

def biggest_range(T):
    n = len(T)
    new = []

    #tworze tablice taką jak startowa ale zawiera dodatkowo informacje jaki ma idx w startowej
    for i in range(n):
        new.append([T[i][0],T[i][1],i]) #lewy indeks, prawy indeks, nr indeksu w startowej tab
    print(new)
    new1 = new[:]

    small_x = Quicksort(new,0,n-1, 0) #tablica posortowana po x, zawiera na ostatnim indeksie ind w oryginalnej
    small_y = Quicksort(new1,0,n-1, 1) #tabilca posortowana po  y, zawiera na ostatnim indeksie ind w oryginalnej
    print(small_x)
    print(small_y)
    #index0-ile istnieje <= x-ow
    #indx1-ile istieje <= y-ow
    #index2-index w oryginalnej
    #index3 - roznica y - x
    cnt = [[0,0,0,0] for _ in range(n)]

    #zliczam ilosc <= x-ow dla danych tablic, dopisuje index oryginalnej tab
    for i in range(n):
        index = small_x[i][2] #jaki miała idx w oryginalnej
        cnt[index][0] = i #ile istnieje tablic które ma mniejszy x
        cnt[index][2] = index #index w oryginalnej

    #zliczam ilosc <= y-ow dla danych tablic
    for i in range(n):
        index = small_y[i][2]
        cnt[index][1] = i #ile istnieje y mniejszych
    print(cnt)

    #zliczam roznice y - x
    for i in range(n):
        cnt[i][3] = cnt[i][1] - cnt[i][0]
    print(cnt)

    #szukam najwiekszej roznicy y - x
    maxi_val = cnt[0][3]
    maxi_ind = cnt[0][2]

    for i in range(1,n):
        if cnt[i][3] > maxi_val:
            maxi_val = cnt[i][3]
            maxi_ind = cnt[i][2]

    return T[maxi_ind]

t = [[6,7],[3,5],[1,6],[2,7]]
print(biggest_range(t))
#najwiecej przedzialow w sobie zawiera [2,7] bo zaiwera 2:[6,7] i [3,5]