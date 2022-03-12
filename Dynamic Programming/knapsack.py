# Problem plecakowy. Na wejściu dostajesz listę wag i cen przedmiotów oraz ograniczenie wagi plecaka.
# Podaj indeksy przedmiotów, których suma cen jest maksymalna i suma wag nie przekracza ograniczenia wagi.

# W - lista wag, P - lista cen
def knapsack(W, P, capacity):
    n = len(W)
    # wiersze to idx przedmiotu do którego rozważamy włącznie
    # kolumny to pojemnosci plecaka do 0 do capacity
    dp = [[0] * (capacity + 1) for _ in range(n)]

    for w in range(W[0], capacity + 1):
        dp[0][w] = P[0]

    for i in range(1, n):
        for w in range(1, capacity + 1):

            if w < W[i]:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - W[i]] + P[i])

    # odtwarza rozwiazanie - indeksy przedmiotow, które nalezy wybrac
    def getSolution(i, capacity):
        if i < 0:
            return []

        elif i == 0:
            if W[0] <= capacity:
                return [0]
            else:
                return

        else:
            if dp[i][capacity] == dp[i - 1][capacity]:
                return getSolution(i - 1, capacity)
            else:
                return getSolution(i - 1, capacity - W[i]) + [i]

    return getSolution(n - 1, capacity)
