# Złodziej widzi na wystawie po kolei n przedmiotów o wartościach A[0], A[1], ..., A[n − 1]. Złodziej
# chce wybrać przedmioty o jak największej wartości, ale resztki przyzwoitości zabraniają mu
# ukraść dwa przedmioty leżące obok siebie. Proszę zaimplementować funkcję:
# int goodThief( int A[], int n );
# która zwraca maksymalną wartość przedmiotów, które złodziej może ukraść zgodnie ze swoim
# kodeksem moralnym oraz wypisuje numery przemiotów które powinien wybrać. Proszę uzasadnić
# poprawność algorytmu oraz oszacować jego złożoność czasową. Algorytm powinien być możliwie
# jak najszybszy (ale przede wszystkim poprawny).

def goodThief(A):
    n = len(A)
    dp = [0] * n
    taken = [False] * n

    dp[0] = A[0]
    dp[1] = max(A[0], A[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + A[i])

    for i in range(n - 1, 1, -1):
        if (dp[i - 2] + A[i] == dp[i]) and (i == n - 1 or taken[i + 1] == False):
            taken[i] = True

    if taken[2] == True:
        taken[0] = True
    else:
        if A[0] > A[1]:
            taken[0] = True
        else:
            taken[1] = True

    for i in range(n):
        if taken[i]:
            print(i, end=" ")
    print()
    return dp[n - 1], dp


t2 = [1, 2, 3, 6, 5]
print(goodThief(t2))
