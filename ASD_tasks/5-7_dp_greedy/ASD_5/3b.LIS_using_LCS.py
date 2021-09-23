# Jak wykorzystać algorytm dla problemu najdłuższego wspólnego podciągu do rozwiązania zadania
# najdłuższego rosnącego podciągu?

#Algorytm działa w ten sam sposób co LCS, przy zapełnianiu tablicy dp porównuje elemnty z tablicy wejściowej
#i posortowanej tablicy wejściowej

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
    
    #zwraca lis
    return res[::-1]

a = [1,9,7,2,0,4,8,6]
print(LIS_uisng_LCS(a))
