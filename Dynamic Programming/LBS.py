#longest bitonic subsequence
#najdluzszy podciag bitoniczny
#ktory najpierw rosnie a potem maleje
#nie musi byc spojny

#obliczam dlg najdluzszego podciagu rosnącego konczacego sie w i
#obliczam najdluzszego podciagu malejacego zaczynajacego sie w i
#potem szukam dla jakiego i suma tych wartosci jest maksymalna
#na podstawie tego indeksu odtwrazam ciąg malejący oraz rosnacy

def LBS(A):
    n = len(A)
    inc = [1] * n #dlg podciagu rosnaego konczacego sie w i
    pi = [-1] * n #ostatni idx w rosnącym
    dec = [1] * n #dlg podciagu malejacego zaczynajacego sie w i
    pd = [-1] * n #pierwszy idx w malejącym

    #szukam najdluzszego podciagu rosnącego konczacego sie w i
    for i in range(1,n):
        for j in range(i):
            if A[i] > A[j] and inc[j] + 1 > inc[i]: #przeszukuje na lewo elementy
                inc[i] = inc[j] + 1
                pi[i] = j

    #szukam najdluzszego podciagu malejacego zaczynajacego sie w i
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            if A[i] > A[j] and dec[j] + 1 > dec[i]: #przeszukuje na prawo elementy
                dec[i] = dec[j] + 1
                pd[i] = j

    #szukam dla jakiego idx suma podciagu rosnącego i malejącego jest maksymalna
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
            if i != maxi: #zeby dwa razy nie wypisac tej samej wartosci
                print(A[i],end=" ")
            solutionDec(pd[i])

    solutionInc(maxi)
    solutionDec(maxi)
    print()

    return inc[maxi] + dec[maxi] #dlg takiego podciagu

A = [4,2,5,7,6,9,1]
print(LBS(A))


