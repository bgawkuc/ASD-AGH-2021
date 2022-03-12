# Dostajesz na wejściu listę A. Grasz z innym graczem w grę, której celem jest zdobycie jak największej ilości punktów.
# Ruch polega na wybraniu jednego z pól - skrajnie lewego lub prawego.
# Zakładając, że przeciwnik gra optymalnie oblicz maksymalną liczbę punktow jaką możesz uzyskać.
# Ty rozpoczynasz grę.

# dp[x][y] - najlepszy wynik gdy gram na planszy zaczynajac sie na idx x i konczacej na idx y

def game(A):
    n = len(A)
    dp = [[0] * n for _ in range(n)]

    # gdy gram na planszy o rozmiarze 1
    for i in range(n):
        dp[i][i] = A[i]

    # gdy gram na planszy o rozmiarze 2
    for i in range(n - 1):
        dp[i][i + 1] = max(A[i], A[i + 1])

    for size in range(2, n):
        for l in range(n):
            r = l + size
            if r < n:
                # gdy wybieram lewy element
                dp[l][r] = max(dp[l][r], A[l] + min(dp[l + 2][r], dp[l + 1][r - 1]))
                # gdy wybieram prawy element
                dp[l][r] = max(dp[l][r], A[r] + min(dp[l][r - 2], dp[l + 1][r - 1]))

    # najlpszy wynik na planszy zaczynajacej sie w idx 0 a konczacej w idx n-1
    return dp[0][n - 1]
