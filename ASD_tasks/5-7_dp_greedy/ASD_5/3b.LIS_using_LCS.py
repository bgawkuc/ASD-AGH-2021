#zloznosc O(n^2)
#najdluzszy rosnacy na bazie najdluzszego wspolnego

#algorytm wygląda tak samo jak algorytm na LCS
#trzeba posortowac wejsciowy ciag rosnący
#tworze tablice rozmiarow jego dlg+1 na jego dlg+1
#tylko jako ciąg A daje posortowany a jako ciąg B nieposortowany
#przechodze po wierszach i kolumnach sprawdzajac ile wynosi obecna dlg wspolnego podciagu

def insertion_sort(A):
    for i in range(1,len(A)):
        new = A[i]
        j = i - 1
        while j >= 0 and A[j] > new:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = new
    return A

def LIS_uisng_LCS(A):
    n = len(A)

    L = [[0] * (n+1) for _ in range(n+1)]

    notsortedA = A[:]

    sortA = insertion_sort(A)


    for i in range(1,n+1):

        for j in range(1,n+1):


            if (notsortedA[i-1] == sortA[j-1]):
                L[i][j] = L[i-1][j-1] + 1

            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])


    return L[n][n]


#CZYTELNIEJSZY ZAPIS I ODTWARZANIE WYNIKU
def lis(A):
    n = len(A)
    # wiersze - A, kolumny - sortA
    dp = [[0] * n for _ in range(n)]

    sortA = A[::]
    sortA = sorted(sortA)

    for i in range(n):
        # 0 kolumna
        if A[i] == sortA[0]:
            dp[i][0] = 1
        # 0 wiersz
        if A[0] == sortA[i]:
            dp[0][i] = 1

    for row in range(1, n):
        for col in range(1, n):
            if A[row] == sortA[col]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

    # odtwarzanie wyniku od końca
    res = []
    row, col = n - 1, n - 1

    while row >= 0 and col >= 0:
        if A[row] == sortA[col]:
            res.append(A[row])
            row -= 1
            col -= 1
        elif dp[row - 1][col] > dp[row][col - 1]:
            row -= 1
        else:
            col -= 1

    return res[::-1], dp[n - 1][n - 1]

a = [1,9,7,2,0,4,8,6]
print(LIS_uisng_LCS(a))
