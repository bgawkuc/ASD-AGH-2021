#Znajdż LBS(longest bitonic subsequence), czyli najdłuższy podciąg, który najpierw rośnie, a potem maleje.


#Obliczam: dlg najdluzszego podciagu rosnącego konczacego sie w i, dlg najdluzszego podciagu malejacego zaczynajacego sie w i.
#Na podstawie tych danych znajduje długość LBS i go odtwarzam.
#Złożoność: O(n^2), n - rozmiar listy wejściowej

def LBS(A):
    n = len(A)
    inc = [1] * n #dlg podciagu rosnacego konczacego sie w i
    pi = [-1] * n #ostatni idx w rosnącym
    dec = [1] * n #dlg podciagu malejacego zaczynajacego sie w i
    pd = [-1] * n #pierwszy idx w malejącym

    #szukam najdluzszego podciagu rosnącego konczacego sie w i
    for i in range(1,n):
        for j in range(i):
            if A[i] > A[j] and inc[j] + 1 > inc[i]:
                inc[i] = inc[j] + 1
                pi[i] = j

    #szukam najdluzszego podciagu malejacego zaczynajacego sie w i
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            if A[i] > A[j] and dec[j] + 1 > dec[i]:
                dec[i] = dec[j] + 1
                pd[i] = j

    #szukam dla jakiego indeksu suma podciagu rosnącego i malejącego jest największa
    maxi = 0
    for i in range(1,n):
        if inc[i] + dec[i] > inc[maxi] + dec[maxi]:
            maxi = i

    #wypisuje podciag rosnący
    def solutionInc(i):
        if pi[i] != -1:
            solutionInc(pi[i])
        print(A[i],end=" ")

    #wypisuje podciąg malejący
    def solutionDec(i):
        if pd[i] != -1:
            if i != maxi:
                print(A[i],end=" ")
            solutionDec(pd[i])

    solutionInc(maxi)
    solutionDec(maxi)
   
