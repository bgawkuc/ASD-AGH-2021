# Dana jest tablica n liczb naturalnych A. Proszę podać i zaimplementować algorytm, który sprawdza, 
# czy da się wybrać podciąg liczb z A, które sumują się do zadanej wartości sum.

#dp[x][y] - czy patrząc na elemnty do indeksu x włącznie da się utworzyć sumę y


def subsetSum(A,sum_):
    n = len(A)
    dp = [[False] *(sum_+1) for _ in range(n+1)] 

    #sumę 0 zawsze się da utworzyć
    for i in range(n+1): 
        dp[i][0] = True

    for i in range(n+1): 
        for j in range(1,sum_+1):

            if j < A[i-1]:
                dp[i][j] = dp[i-1][j]

            #gdy jest szansa by zabrac moją i-tą liczbe
            else:
                dp[i][j] = (dp[i-1][j] or dp[i-1][j-T[i-1]])
                

    return dp[n][sum_]
