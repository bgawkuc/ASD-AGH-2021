# Problem plecakowy - dwuwymiarowa wersja problemu - oprócz ciężaru jest wysokość towarów.
# {p1, ..., pn} - przedmioty v(pi) - wartość przedmiotu pi
# r(pi) - ciężar przedmiotu pi h(pi) - wysokość przedmiotu pi
# Jaka jest największa możliwa sumaryczna wartość przedmiotów, których ciężar
# nie przekracza M a wysokość S?


def knapsack2d(P, W, H, maxW, maxH):
    n = len(P)

    # dp[i][h][w] - max zarobek gdy patrze do i-tego przedmiotu majac max wage w i max wysokosc h
    dp = [[[0 for _ in range(maxH + 1)]
           for _ in range(maxW + 1)]
          for _ in range(n)]

    for w in range(W[0], maxW + 1):
        for h in range(H[0], maxH + 1):
            dp[0][w][h] = P[0]

    # i-idx obecnie rozpatrywanego przedmiotu
    # w-waga obecnie rozpatrywanego przedmiotu
    # h-wysokość obecnie rozpatrywanego przedmiotu
    for i in range(1, n):
        for w in range(maxW + 1):
            for h in range(maxH + 1):

                dp[i][w][h] = dp[i - 1][w][h]
                if W[i] <= w and H[i] <= h:
                    dp[i][w][h] = max(dp[i][w][h], dp[i - 1][w - W[i]][h - H[i]] + P[i])

    return dp[n - 1][maxW][maxH]


P = [10, 4, 7, 8]
H = [6, 1, 3, 5]
W = [6, 3, 1, 5]

# max profit 12: biore przedmioto idx 1 i 3
# waga: 3 + 5 < 10
# wysokosc: 1 + 5 <= 6
print(knapsack2d(P, W, H, 10, 6))
