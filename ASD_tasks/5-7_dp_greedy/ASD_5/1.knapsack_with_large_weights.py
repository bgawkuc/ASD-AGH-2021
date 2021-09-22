#problem plecakowy
#dobre rzowizanie dla duzych wag bo zlozonosc to O(n*sumawszystkichprofitów)
#tworze tablice o wymiarach n na sumprofits + 1
#moge wybrac tylko 1 przedmiot kazdego rodzaju
#sprawdzam czy jego profit jest <= od kolummy
#jesli tak to wpisuje jego wage
#jak nie to reszta wiersza ma wartosc inf
#tak uzupelniam wiersz o ind 0
#tabela bedzie zapalniona wagami
#a kolumny oznaczaja ile wynosi profit w tym momencie
#a wiersze na jakim ind przedmiotu skonczylismy

#i-indeks, p-profit
#f(i,p) min waga z przedmiotow 0,...,i osiagajacych profit = p
#f(0,p) = 0, p = 0
#f(0,p) = inf, p > 0
#f(i,0) = 0
#f(i,p) = f(i-1,p), p < P[i]
#f(i,p) = min(f(i-1,p), f(i-1,p-P[i]+W[i]))
#wynik to max( p | f(i,p) <= W) w ostatnim wierszu szukam wart kol gdzie spelnia waga <=

#CZYTELNIEJSZA IMPLEMENTACJA
def knapsack2(P, W, maxWeight):
    n = len(P)
    sumProf = sum(P)
    dp = [[float('inf')] * (sumProf + 1) for _ in range(n)]

    # dla profitu 0 waga produktów wynosi 0
    for i in range(n):
        dp[i][0] = 0

    # zapełniam wiersz dla przedmiotu 0, dopoki jego profit jest >= ogolnego profitu to go wybieram
    for i in range(1, sumProf + 1):
        if P[0] >= i:
            dp[0][i] = W[0]
        else:
            break

    for idx in range(1, n):
        for profit in range(sumProf + 1):

            # gdy profit przedmiotu przekracza obecny profit
            # to albo biore to co bylo przed albo jego samego
            if P[idx] > profit:
                dp[idx][profit] = min(dp[idx - 1][profit], W[idx])
            # to sprawdzam kiedy osiągne mniejszą wage: gdy wybiore przedmiot idx czy nie
            else:
                dp[idx][profit] = min(dp[idx - 1][profit], dp[idx - 1][profit - P[idx]] + W[idx])

    # szukam kolumny dla którj waga jest <= maxWeight a nr kolumny(<=> suma profitów)
    # jest mozliwie jak największa
    right = dp[n - 1][sumProf]
    left = dp[n - 1][sumProf - 1]
    last = None

    # gdy w ostatniej kolumnie i ostatnim wierszu waga jest mniejsza lub rowna maksymalnej wadze
    if right == maxWeight or (left <= maxWeight and right <= maxWeight):
        last = sumProf

    # szukam kolumny która wyznacza mi profit czy danym ogranniczeniu na maxWeight
    for i in range(sumProf - 2, -1, -1):
        if last is None:
            right = left
            left = dp[n - 1][i]

            if right == maxWeight or (left <= maxWeight and right <= maxWeight):
                last = i + 1
                break

    # na podstawie profitu <=> nr kolumny odtwarzam rozwiazanie - wybrane indeksy
    def solution(i, profit):
        if i < 0:
            return []
        elif i == 0:
            if P[0] <= profit:
                return [0]
            return []
        elif dp[i][profit] == dp[i - 1][profit]:
            return solution(i - 1, profit)
        else:
            return solution(i - 1, profit - P[i]) + [i]

    # profit,wybrane indeksy
    return last, solution(n - 1, last)


W = [4, 5, 12, 9, 1, 13]
P = [10, 8, 4, 5, 3, 7]
print(knapsack2(P, W, 10))


#MNIEJ CZYTELNA IMPLEMENTACJA
def getSolution(F, W, P, i, p):
    if i < 0: return []

    if i == 0:
        if p != 0: return [0]
        return []

    if F[i][p] != F[i - 1][p]:
        return getSolution(F, W, P, i - 1, p - P[i]) + [i]
    return getSolution(F, W, P, i - 1, p)


def knapsack(W,P,MaxW):
    n = len(W)
    sumProfits = 0

    for i in range(n):
        sumProfits += P[i]

    #kolumna to profit,wiersz idx przedmiotu
    F = [[999] * (sumProfits+1) for _ in range(n)] #zapelniam bardzo duzymi wartosciami

    for i in range(n): #dla profitu 0 trzeba wybrac 0 elementow o wadze 0
        F[i][0] = 0

    #dopoki profit el o idx 0 jest wiekszy lub rowny od aktualnego profitu (nr kol) to mogę go wybrać samego
    for i in range(1,sumProfits+1):
        if P[0] >= i:
            F[0][i] = W[0]
        else: break

    curr_cost = P[0] #obecny koszt

    for i in range(1,n):
        curr_cost += P[i]
        #moge sprawdzac tylko do currcost bo nie da sie wziac wiekszego profitu
        #v- to nr olumny ktory okresla profit
        for v in range(1,curr_cost+1): #v-profit

            F[i][v] = F[i-1][v]

            # gdy profit przekroczy P[i] tzn ze i-ty przedmiot moze sie w nim zawierac ale nie musi
            if v >= P[i]:
                F[i][v] = min(F[i][v], F[i - 1][v - P[i]] + W[i])
            #gdy profit jest wiekszy od wagi to albo go nie biore albo biore go samego
            else: # v < P[i]
                F[i][v] = min(F[i][v],W[i]) #wybieram to co nade mna lub wage aktualna

    for i in range(n):
        print(F[i])


    #odpowiedzi wysatrczy szukac w ostatnim wierszu bo tu sa mozliwe wagi rozparzenia n elementow
    right = F[n-1][sumProfits] # ostatnia kol
    left = F[n-1][sumProfits-1] #przedostatnia kol

    #gdy wartosc w ostatniej kolumnie <= maxW to maxProf bedzie suma prof(da sie wybrac wszystkie el)
    if right == MaxW or (left <= MaxW and right <= MaxW):
        return sumProfits

    #gdy chce wypisac tylko profit
    #szuak dla jakiej kolumny wartosc w ostatnim wierszu <= maxW
    for i in range(sumProfits - 2,-1,-1):
        right = left
        left = F[n-1][i]
        #szukam takiej kolumny w ostatnim wierszu ze wartosc pola jest <= maxW
        if right == MaxW or (left <= MaxW and right <= MaxW):
            return i + 1

    #gdy chce wypisac profit i liste el
    for i in range(sumProfits + 1):
        if F[n - 1][i] > MaxW:
            print(getSolution(F, W, P, n - 1, i - 1))
            return i - 1
    return 0



W = [4,5,12,9,1,13]
P = [10,8,4,5,3,7]
print(knapsack(W,P,10))
