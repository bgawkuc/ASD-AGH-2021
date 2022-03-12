# sortowanie przez zliczanie
# złożoność: O(n+k), n-rozmiar listy, k-największa wartość w liście

def countingSort(A):
    n = len(A)
    k = max(A)
    cnt = [0] * (k + 1)
    output = [0] * n

    # zliczam ilość wystąpień każdej liczby
    for i in range(n):
        cnt[A[i]] += 1

    for i in range(1, k + 1):
        cnt[i] += cnt[i - 1]

    for i in range(n - 1, -1, -1):
        cnt[A[i]] -= 1
        output[cnt[A[i]]] = A[i]

    return output
