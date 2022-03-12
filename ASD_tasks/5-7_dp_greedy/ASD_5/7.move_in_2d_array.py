# Dana jest szachownica A o wymiarach m x n. Szachownica
# zawiera liczby wymierne. Należy przejść z pola (0, 0) na pole (m, n) korzystając jedynie z ruchów “w dół”
# oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
# znajdujący trasę o minimalnym koszcie

#tworzę tablice dp rozmiaru takiego tak wejściowa
#dp[i][j] - koszt dotarcia do pola o współrzędnych (i,j)

def chessboard(C):
    m = len(C)
    n = len(C[0])
    dp = [[0] * n for _ in range(m)]

    for j in range(n):
        dp[0][j] = dp[0][j-1] + C[0][j]

    for i in range(m):
        dp[i][0] = dp[i-1][0] + C[i][0]

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + C[i][j]
            
    return dp[m-1][n-1]
