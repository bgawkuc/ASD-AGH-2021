#suma podzbioru
#czy istnieje podciag(nie musi byc spojny) sumujacy sie do zadanej sumy
#wiersze odpowiadaja wartosciom w tablicy
#kolumny odpowiadaja czy da sie stworzyc odpoweiednia sume
#analogiczne rozwiazanie jak knapsack
#zlozonosc O(n*sum)
#f(i,j) czy istnieje suma w podzbiorze {a0,..,ai-1} o wartosci j
#f(0,0) = T
#f(0,j) = F, j > 0
#f(i,0) = T
#4)F(i,j) = F[i-1][j] or F[i-1][j-T[i-1]], j >=T[i-1]

#czyli ta tablica 2d mowi mi
#i-wiersze, nr przedmiotu na jakim koncze, j-kolummny, suma jaką chce uzyskac
#czy mając do wyboru przedmiotu do tego nr i włącznie z tablicy to moge utworzyc sume j
#gdy suma j jest < od mojego obenego to spisuje wynik jaki jest nade mna
#czyli dla tej samej sumy ale konczac na i - 1 przedmiocie
#gdy suma >= j to biore maxa z okienka nade mną
#oraz z wziecia pola wartosci jakiej brakuje:
#wiersz i - 1; kolumna suma - moc obecnego

def subsetSum(T,sum):
    n = len(T)
    F = [[False] *(sum+1) for _ in range(n+1)] #tworze tablice 2d o wymiarach n+1 na sum+1

    for i in range(n+1): #sume 0 da sie utworzyc konczac na dowolnej wartosci z T bo nie musze nic wybrac
        F[i][0] = True

    #i-kolejne wartosci z T na ktorych koncze sprawdzanie ,wiersze
    #j-obecna max suma, kolumny
    for i in range(n+1): #numery liczb z tablicy T
        for j in range(1,sum+1): #obecna wartosc sumy

            #jesli wartosc mojego obecnego przedmiotu jest za duza od obecnej sumy
            #to nie da sie wybrac i-tego przedmiotu wiec wynik jest taki sam jak przedmiotu i-1
            if j < T[i-1]:
                F[i][j] = F[i-1][j]

            #gdy jest szansa by zabrac moją i-tą liczbe
            else:
                F[i][j] = (F[i-1][j] or F[i-1][j-T[i-1]])
                #sprawdzam czy choc jedno da mi true
                #albo opcja gdy nie biore mojego obecnego przedmiotu
                #albo gdy gdy biorę(to spr wtedy wartosc bool dla lizby jaką nalezy dodac do T[i-1] by otrzymac j)
                #gdyby choc jedno z nich bylo True to dostanie True

    for i in range(n+1): #wyswietla koncowa tablice
        print(F[i])

    return F[n][sum] #wynik(bool)

#BARDZIEJ ZROZUMIAŁA IMPLEMENTACJA
def subsetSum2(A,s):
    n = len(A)
    dp = [[False] * (s+1) for _ in range(n)]

    #gdy mam tylko el o idx 0 to sie da stworzyc sume o wartosci A[0]
    dp[0][A[0]] = True

    #zawsze da sie uzyskac sume 0
    for i in range(n):
        dp[i][0] = True


    for idx in range(1,n):
        for sum_ in range(1,s+1):

            #gdy wartosc el jest <= obecnej sumy
            if A[idx] <= sum_:
                #to nie biore lub biore ten el
                dp[idx][sum_] = dp[idx-1][sum_] or dp[idx-1][sum_-A[idx]]
            #gdy el jest za duzy w stosunku do obecnej sumy
            else:
                #to nie biore el
                dp[idx][sum_] = dp[idx-1][sum_]
    return dp[n-1][s]


t = [2,3,7,8,10]
print(subsetSum(t,15))


