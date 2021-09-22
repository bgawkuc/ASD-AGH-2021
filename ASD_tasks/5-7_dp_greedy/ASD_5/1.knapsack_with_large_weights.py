# Proszę podać i zaimplementować algorytm znajdujący wartość optymalnego zbioru przedmiotów w dyskretnym problemie plecakowym. 
# Algorytm powinien działać w czasie wielomianowym względem liczby przedmiotów oraz sumy ich profitów

#dp[x][y] - minimalna sumaryczna waga przedmiotów gdy patrzę do indeksu x mając sume profitów wartości y

def knapsack2(P, W, maxWeight):
    n = len(P)
    sumProf = sum(P)
    dp = [[float('inf')] * (sumProf + 1) for _ in range(n)]

    # dla profitu 0 waga produktów wynosi 0
    for i in range(n):
        dp[i][0] = 0

    for i in range(1, sumProf + 1):
        if P[0] >= i:
            dp[0][i] = W[0]
        else:
            break

    for idx in range(1, n):
        for profit in range(sumProf + 1):

            # gdy profit przedmiotu przekracza obecny profit
            if P[idx] > profit:
                dp[idx][profit] = min(dp[idx - 1][profit], W[idx])
            else:
                dp[idx][profit] = min(dp[idx - 1][profit], dp[idx - 1][profit - P[idx]] + W[idx])

    #szukam jaki max profit mogę uzyskac biorąc pod uwagę wszystkie przedmioty i ograniczenie wagi
    right = dp[n - 1][sumProf]
    left = dp[n - 1][sumProf - 1]
    last = None

    if right == maxWeight or (left <= maxWeight and right <= maxWeight):
        last = sumProf

    for i in range(sumProf - 2, -1, -1):
        if last is None:
            right = left
            left = dp[n - 1][i]

            if right == maxWeight or (left <= maxWeight and right <= maxWeight):
                last = i + 1
                break
                
    #odtwarza indeksy wybranych przedmiotów
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

    return solution(n - 1, last)
