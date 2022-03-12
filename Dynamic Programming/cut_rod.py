# Dostaje tablicę A. A[i] - zarobek za kawałek długości i. Oblicz max zarobek za pocięcie pręta długości len(A)-1.

# dp[i] - max zarobek za pocięcie pręta długości i

def cutRod(A):
    n = len(A)
    dp = A[:]

    for i in range(2, n):
        for cut in range(i):
            dp[i] = max(dp[i], A[cut] + dp[i - cut])
    return dp[-1]
