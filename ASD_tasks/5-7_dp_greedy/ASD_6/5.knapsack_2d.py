#dwuwymiarowy problem
#mam ograniczenie w plecaku na wage i wysokosc
#wyznacz max profit

def knapsack(P, W, H, maxWeight, maxHeight):
    n = len(P)
    # dp[i][w][h] - max profit gdy patrze do i-tego przedmiotu włącznie
    # do wagi w i wys h
    dp = [[[0 for _ in range(maxHeight + 1)]
           for _ in range(maxWeight + 1)]
          for _ in range(n)]

    # gdy zerowy przedmiot się zmiesci
    for w in range(W[0], maxWeight + 1):
        for h in range(H[0], maxHeight + 1):
            dp[0][w][h] = P[0]

    for i in range(1, n):
        for w in range(maxWeight + 1):
            for h in range(maxHeight + 1):

                # gdy i-ty przedmiot sie zmiesci
                #to sprawdzam czy bardziej sie oplaca go wybierać czy nie
                if W[i] >= w and H[i] >= h:
                    dp[i][w][h] = max(dp[i][w][h], dp[i - 1][w - W[i]][h - H[i]] + P[i])
                else:
                    dp[i][w][h] = dp[i - 1][w][h]

    return dp[n - 1][maxWeight][maxHeight]