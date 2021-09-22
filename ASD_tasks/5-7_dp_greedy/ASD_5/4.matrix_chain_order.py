#w jakiej kolejnosci nalezy wymnozyc macierze by koszt tego dzialania byl mozliwie jak najmnijeszy
#t=[1,2,3,4] tzn ze macierze maja wymiar 1x2, 2x3, 3x4
#macierze numeruje a1,a2,a3...
#el tablicy numeruje d0,d1,d2...

def matrixChainOrder(p):
    n = len(p)

    dp =[[0 for _ in range(n+1)] for _ in range(n+1)]
    res =[[0 for _ in range(n+1)] for _ in range(n+1)] #tu zapisuje indeks od ktorego dziele

    for j in range(1, n): #j to roznica indeksow miedzy macierzami,czyli ile macierzy moze objac nawias
        for i in range(1,n + 1 - j): #to nr macierzy od ktorej zaczynam

            k = i + j

            #nie trzeba dodawac dwoch wartosci z dp bo jedna z nich zawsze wyniesie 0(dp[i][i] i dp[k][k] da sie pominac)
            dp[i][k] = min(dp[i + 1][k] + dp[i][i] + p[i - 1][0] * p[i-1][1] * p[k-1][1], #kiedy stawiam nawiasr od i+1 do k
                               dp[i][k - 1] + dp[k][k] + p[i - 1][0] * p[k - 1][0] * p[k-1][1]) #kiedy stawiam nawias od i do k-1

            #zapamietuje od jakiego indeksu dziele tab
            if dp[i + 1][k] + dp[i][i] + p[i - 1][0] * p[i-1][1] * p[k-1][1] < dp[i][k - 1] + dp[k][k] + p[i - 1][0] * p[k - 1][0] * p[k-1][1]:
                res[i][k] = i-1
            else:
                res[i][k] = k-1

    #sposob gdy mam tab w postaci [1,2,3...]
    # for j in range(1, n - 1): #j to roznica indeksow miedzy macierzami,czyli ile macierzy moze objac nawias
    #     for i in range(1,n - j): #to nr macierzy od ktorej zaczynam
    #
    #         k = i + j
    #
    #         #nie trzeba dodawac dwoch wartosci z dp bo jedna z nich zawsze wyniesie 0(dp[i][i] i dp[k][k] da sie pominac)
    #         dp[i][k] = min(dp[i + 1][k] + dp[i][i] + p[i - 1] * p[i] * p[k], #kiedy stawiam nawiasr od i+1 do k
    #                            dp[i][k - 1] + dp[k][k] + p[i - 1] * p[k - 1] * p[k]) #kiedy stawiam nawias od i do k-1

    for i in range(n+1):
        # print(dp[i])
        print(res[i])

    sol = [0] * n
    ind = n - 1

    #wypisuje odp
    for i in range(n,2,-1):
        sol[ind] = p[res[1][i]]
        p[res[1][i]] = -1
        ind -= 1

    ind = 0
    for i in range(n):
        if p[i] != -1:
            sol[ind] = p[i]
            ind += 1

    return dp[1][n], sol


#ŁADNIEJSZY ZAPIS, ALE BEZ ODTWARZANIA WYNIKU
#głowna przekatna gdy biore 2 nawiasy
#mniejsza gdy biore 3 nawiasy
#kolejna gdy 4 itd
#l-numer nawiasu na ktorym zaczynam(moge zaczac od 1 dopiero)
#r-numer nawiasu na ktorym koncze(moge skonczyc na n-tym)

def matrixChainOrder2(A):
    n = len(A)
    #dp[l][r] - min wartosc mnozenia macierzy gdy biore nawiasy od l-tego do r-tego (włącznie)
    dp = [[0] * (n+1) for _ in range(n+1)]
    res = [[0] * (n+1) for _ in range(n+1)]

    for j in range(1,n): #ile macierzy obejmuje obecnie mnozenie
        for l in range(1,n + 1 -j): #numer pierwszej macierzy(nie idx!!!)
            r = l + j #numer ostatniej macierzy (nie idx!!)

            #dp[l][r] najmniejszy wynik gdy mnoze macieze od idx l do idx r
            #1 opcja: mam wymnozone macierze od l+1 do r, dodaje do tego macierz l i sume z mnozenia 2 nawiasów
            #-nawiasu 'lewego' z 'prawym'
            #2 opcja: mam wymnozone macierze od l do r-1, dodaje do tego macierz r i sume z mnozenia 2 nawiasów
            #-nawiasu 'prawego' z 'lewym'
            dp[l][r] = min(dp[l+1][r] + dp[l][l] + A[l-1][0] * A[l-1][1] * A[r-1][1],
                           dp[l][r-1] + dp[r][r] + A[l-1][0] * A[r-1][0] * A[r-1][1])

            #gdy 1 opcja jest 'tansza' od 2 opcji
            if dp[l+1][r] + dp[l][l] + A[l-1][0] * A[l-1][1] * A[r-1][1] < dp[l][r-1] + dp[r][r] + A[l-1][0] * A[r-1][0] * A[r-1][1]:
                #idx macierzy który dzielił
                #tu dzielila macierz numer l na macierze l i od l+1 do r
                res[l][r] = l-1
            else:
                #tu dzieliła macierz numer r na macierze od l do r-1 i r
                res[l][r] = r-1

    #wynik-min wartosc mnozenia gdy biore macierze od pierwszej do n-tej
    return dp[1][n]


a = [[3,2],[2,4],[4,2],[2,5]] #max 58
b = [[1,2],[2,3],[3,4]] #max 18
c = [[10,30],[30,5],[5,60]]
print(matrixChainOrder(a))



