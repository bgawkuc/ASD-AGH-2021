# Dostajesz na wejsciu wyaz zlozony z liter a-z. Zwroc jego najdłuższy (spójny) fragment, ktory jest palindromem.
# Palindrom - wyaz czytany od lewej i od prawej brzmi tak samo.

# dp[i][j] czy slowo zaczynajace sie na indeksie i a konczace na indeksie j jest palindromem
# zloznosc o(n^2)

def palindrome(A):
    n = len(A)
    dp = [['F'] * n for _ in range(n)]
    start = end = 0
    l = 1

    # slowa 1literowe są palindromami
    for i in range(n):
        dp[i][i] = 'T'

    # slowa 2literowe są palinromami wtw gdy obie litery są takie same
    for i in range(n - 1):
        if A[i] == A[i + 1]:
            dp[i][i + 1] = 'T'
            if l < 2:
                start = i
                end = i + 2
                l = 2

    for length in range(n):
        for l in range(n):
            r = l + length
            if l > 0 and r < n - 1:

                # jesli slowo od l do r jest palindromem i litery mające indeks l-1 i r+1 są takie same
                # to słowo od indeksu l-1 do r+1 jest palindromem
                if dp[l][r] == 'T':
                    if A[l - 1] == A[r + 1]:
                        dp[l - 1][r + 1] = 'T'
                        if r + 1 - (l - 1) + 1 > l:
                            start = l - 1
                            end = r + 1
                            l = r + 1 - (l - 1) + 1

    return A[start:end + 1]
