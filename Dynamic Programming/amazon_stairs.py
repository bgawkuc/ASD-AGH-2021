# Dostaje listę A wypełnioną liczbami.
# A[i] - maksymalna długość skoku jaką mogę wykonać z i-tego pola.
# Podaj ilość sposobów na jakie mogę się dostac z pierwszego pola na ostatnie.

# dp[i] - ilosc sposobów na jakie mogę się dostać z i-tego pola na ostatnie
# złożoność: O(n^2)

def cntWays(A):
    n = len(A)
    dp = [0] * n
    dp[n - 1] = 1

    for i in range(n - 2, -1, -1):
        for j in range(1, A[i] + 1):
            # próbuje wykonać skok z pola o indeksie i długości j
            if j + i < n:
                dp[i] += dp[i + j]

    return dp[0]
