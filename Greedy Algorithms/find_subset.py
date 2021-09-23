#dany jest zbior przedziałow otwarych
#zaproponuj algorytm ktory znajdzie podzbior tego zbioru taki ze:
#1)jego rozmiar wynosi k
#2)przedialy sa rozlaczne
#3)roznica miedzy najwczeniejszym poczatkiem a najdalszym koncem jest minimalna

#sortuje przedialy po początkach za pomocą quicksorta
#dla kazdego przedziału znajduje kolejny
#kolejny to taki ktory zaczyna sie pozniej niz poprzedni konczy
#a koniec kolejenego jest mozliwie jak najmniejszy
#przechodze po tablicy i sprawdzam czy zaczyanajac od i-tego pzechodzac po kolejnych uzyskam rozmiar k
#jesli tak to sprawdzam czy roznica miedzy koncem a poczatkiem jest mniejsza od ostatnio zapisanej
#zwracam zbior przedziałów dla których ta roznica była minimalna

def partition(A,l,r):
    piv = A[r]
    i = l
    for j in range(l,r):
        if A[j][0] < piv[0]:
            A[i],A[j] = A[j],A[i]
            i += 1
    A[i],A[r] = A[r],A[i]
    return i


def quicksort(A,l,r):
    if l < r:
        q = partition(A,l,r)
        quicksort(A,l,q-1)
        quicksort(A,q+1,r)


def findSubset(A,k):
    n = len(A)
    #sortuje quicksortem zeby patrzyl tez na 1 indeks
    #jesli 2 przedziały mają taki sam 0 idx to wczesniej będzie ten co ma mniejszy idx 1
    quicksort(A,0,n-1)

    #indeks kolejnego przedziału, który zaczyna sie pozniej niz konczy i-ty i ma minimalny koniec
    next = [None] * n

    #i-startowy indeks
    for i in range(n):
        nextEnd = None
        for j in range(i+1,n):
            #jesli znajde 1 kolejny przedział lub przedział o mniejszym koncu to go aktualizuje
            #oraz ten przedział ma poczatek wiekszy od i-tego konca
            if (nextEnd is None or A[j][1] < A[nextEnd][1]) and A[i][1] <= A[j][0]:
                nextEnd = j
        next[i] = nextEnd

    #najmiejsza roznica miedzy koncem a początkiem
    bestDiff = float('inf')
    res = []

    #szukam zbioru przedziałow o rozmiarze k i min roznicy miedzy poczatkiem a koncem
    for i in range(n):
        #poczatek, koniec zbioru przedziałów
        start = A[i][0]
        end = A[i][1]
        #obecny rozmiar zbioru przedziałów
        size = A[i][1] - A[i][0]
        idx = i
        #zbior przediałów
        currRes = [A[i]]

        #dopoki rozmiar przedziałow jest mniejszy od k
        while size < k:
            #gdy istnieje kolejny przedział
            if next[idx] is not None:
                #przechodze do niego
                idx = next[idx]
                #dodaje jego rozmiar
                size += (A[idx][1]-A[idx][0])
                #ustawiam jego jako koniec zbioru przedziałów
                end = A[idx][1]
                #dodaje przedział do listy wynikowej
                currRes.append(A[idx])
            else:
                break

        #jesli znalazlam zbior przedziałów rozmiaru k
        if size == k:
            #gdy ten zbior ma mniejszą roznice niz ostatnio zapisany
            if end - start < bestDiff:
                bestDiff = end-start
                res = currRes

    #gdy znalazlam rozwiazanie
    if len(res):
        return res
    #gdy zadne przedziały nie sumują sie do rozmiaru k
    return None

A = [[4,5],[1,3],[1,2],[7,9],[7,8]]
print(findSubset(A,3))