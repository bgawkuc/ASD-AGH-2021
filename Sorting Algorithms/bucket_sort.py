# sortowanie kubełkowe
# zlożoność: O(n) dla rozkladu jednostajnego

def bucketSort(A):
    n = len(A)
    # tworze n kubełków i na bazie wartości dodaje wartości z A do odpowiednich
    buckets = [[] for _ in range(n)]
    maxi = max(A)
    mini = min(A)
    r = (maxi - mini) / n

    if r == 0:
        return A

    for i in range(n):
        d = (A[i] - mini) / r - int((A[i] - mini) / r)

        # ustalam indeks kubełka, do którego trafi i-ty element listy
        if d == 0 and A[i] != mini:
            bucketIdx = int((A[i] - mini) / r) - 1
        else:
            bucketIdx = int((A[i] - mini) / r)

        buckets[bucketIdx].append(A[i])

    output = []

    # każdy kubełek sortuje i dodaje do listy wynikowej
    for i in range(n):
        buckets[i].sort()
        output.extend(buckets[i])

    return output
