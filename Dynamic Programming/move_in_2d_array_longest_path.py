#Na wejściu dostajesz znajduje się tablica 2d - A, każde pole posiada wartość.
#Po tablicy można się poruszać po polach o wspólnych bokach, z pól o mniejszej wartości na większe.
#Znajdź maksymalną długość ścieżki.

#dp[x][y] - dlugość najdłuższej ścieżki zaczynającej się w polu o współrzędnych x,y

def bestPath(A):
    n = len(A)
    m = len(A[0])
    dp =[[None] * m for _ in range(n)]
    maxi = 0

    def isIn(i,j):
        return 0 <= i < n and 0 <= j < m

    #oblicza długość sciezki zaczynajacej sie w polu o współrzędnych i,j
    def pathValue(i,j):
        if not isIn(i,j):
            return 0
        #gdy pole jest policzone
        if dp[i][j] is not None:
            return dp[i][j]

        up = left = right = down = 1

        if isIn(i-1,j) and A[i-1][j] > A[i][j]:
            down = 1 + pathValue(i-1,j)
        if isIn(i+1,j) and A[i+1][j] > A[i][j]:
            up = 1 + pathValue(i+1,j)
        if isIn(i,j-1) and A[i][j-1] > A[i][j]:
            left = 1 + pathValue(i,j-1)
        if isIn(i,j+1) and A[i][j+1] > A[i][j]:
            right = 1 + pathValue(i,j+1)

        dp[i][j] = max(down,max(up,max(left,max(right,1))))
        return dp[i][j]

    #wypełnia tablice dp
    for i in range(n):
        for j in range(m):
            if dp[i][j] is None:
                dp[i][j] = pathValue(i,j)
            maxi = max(maxi,dp[i][j])

    return maxi
