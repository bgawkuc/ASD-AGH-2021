#sortowanie kubełkowe
#zlożoność: O(n) dla rozkladu jednostajnego

def bucketSort(A):
    n = len(A)
    buckets = [[] for _ in range(n)]
    maxi = max(A)
    mini = min(A)
    r = (maxi - mini) / n

    if r == 0:
        return A

    for i in range(n):
        d = (A[i] - mini) / r - int((A[i] - mini) / r)

        if d == 0 and A[i] != mini:
            bucketIdx = int((A[i] - mini) / r) - 1
        else:
            bucketIdx = int((A[i] - mini) / r)

        buckets[bucketIdx].append(A[i])

    output = []

    for i in range(n):
        buckets[i].sort()
        output.extend(buckets[i])

    return output
