# Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce,
# żeby wjechać na prom. Prom ma dwa pasy (lewy i prawy), oba długości L. Proszę napisać program, który
# wyznacza, które samochody powinny pojechać na który pas, żeby na promie zmieściło się jak najwięcej aut.
# Auta muszą wjeżdżac w takiej kolejności, w jakiej są podane w tablicy A.

#dp[i][j] - czy na pokład dlugosci j wjadą auta od indeksu 0 do i z A

def ferry(A, length):
    n = len(A)

    # pref[i] - suma dlugosci aut od indeksu 0 do i
    pref = [0] * n
    pref[0] = A[0]
    for i in range(1, n):
        pref[i] = pref[i - 1] + A[i]

    dp = [[False] * (length + 1) for _ in range(n)]

    for i in range(A[0], length + 1):
        dp[0][i] = True

    for idx in range(n - 1):
        for l in range(1, length + 1):

            if dp[idx][l]:
                # na lewy pas próbuje wpuscic auto o indeksie idx
                if l + A[idx + 1] <= length:
                    dp[idx + 1][l + A[idx + 1]] = True

                # na prawy pas próbuje wpuścić auto o indeksie idx
                if pref[idx + 1] - l <= length:
                    dp[idx + 1][l] = True

    idx = n - 1
    while dp[idx][length] is False:
        idx -= 1

    # zwraca indeks ostatniego auta jakie wjechało na prom
    return idx
