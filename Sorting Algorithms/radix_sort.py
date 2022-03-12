# sortowanie pozycyjne
# jest to counting sort wywołany d razy
# gdzie d to ilość cyfr w największej liczbie
# złożoność: O(d*(n+k)), k - zakres liczb (od 0 do 9)

# l-wskazuje po jakiej cyfrze sortuje
def countingSort(A, l):
    n = len(A)
    cnt = [0] * 10
    output = [0] * n

    for i in range(n):
        j = (A[i] // l) % 10
        cnt[j] += 1

    for i in range(1, 10):
        cnt[i] += cnt[i - 1]

    for i in range(n - 1, -1, -1):
        j = (A[i] // l) % 10
        cnt[j] -= 1
        output[cnt[j]] = A[i]

    A[:] = output


def radixSort(A):
    l = 1
    while max(A) // l > 0:
        countingSort(A, l)
        l *= 10
    return A
