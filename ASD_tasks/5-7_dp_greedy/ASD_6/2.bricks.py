# Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1, b1], [a2, b2], . . ., [an, bn]. 
# Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować algorytm, który oblicza ile klocków 
# należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił  się w całości w tam, który spadł tuż przed nim.

#dp[i] - maksymalna wysokość wieży kończąca się na klocku o indeksie i

def bricks(A):
    n = len(A)
    dp = [1] * n

    for i in range(1,n): 
        for j in range(i):
            #klocek o indeksie j musi mieć większe rozmiary niż ten o indeksie i
            #oraz musi powiększać wysokość wieży
            if A[i][0] >= A[j][0] and A[i][1] <= A[j][1] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return n - max(dp)
