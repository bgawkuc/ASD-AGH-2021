# Proszę zaproponować algorytm dla dwuwymiarowej wersji dyskretnego problemu plecakowego.
# Mamy dany zbiór n przedmiotów i dla każdego przedmiotu dane sa nastepujace trzy liczby: 
# P[i] - cena, W[i] - waga, H[i] - wysokosć. Mamy ograniczenie plecaka w postaci maksymalnej wagi i wysokości.

#dp[i][w][h] - max zysk jaki da sie uzyskac patrzac na przedmioty o indeksach od 0 do i oraz mając ograniczenie wagi w i wysokosci h

def knapsack(P, W, H, maxWeight, maxHeight):
    n = len(P)

    dp = [[[0 for _ in range(maxHeight + 1)]
           for _ in range(maxWeight + 1)]
          for _ in range(n)]

    for w in range(W[0], maxWeight + 1):
        for h in range(H[0], maxHeight + 1):
            dp[0][w][h] = P[0]

    for i in range(1, n):
        for w in range(maxWeight + 1):
            for h in range(maxHeight + 1):

                if W[i] >= w and H[i] >= h:
                    dp[i][w][h] = max(dp[i][w][h], dp[i - 1][w - W[i]][h - H[i]] + P[i])
                else:
                    dp[i][w][h] = dp[i - 1][w][h]

    return dp[n - 1][maxWeight][maxHeight]
