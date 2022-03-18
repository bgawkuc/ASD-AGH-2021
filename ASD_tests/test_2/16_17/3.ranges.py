## Zbiór przedziałów {[a1, b1], ..., [an, bn]}, każdy przedział należy do [0, 1]. Opisać algorytm który
# sprawdzi czy jest możliwy taki wybór przedziałów, aby cały przedział [0, 1] zawierał się w
# wybranych odcinkach. Przedział ma składać się z jak najmniejszej ilości odcinków.


def binarySearch(A, l, r, x):
    if l <= r:
        mid = l + (r - l) // 2
        if x <= A[mid][0] and (mid == 0 or x > A[mid - 1][0]):
            return mid
        elif x <= A[mid][0] and x <= A[mid - 1][0]:
            return binarySearch(A, l, mid - 1, x)
        else:
            return binarySearch(A, mid + 1, r, x)
    return None


def ranges(A, k):
    n = len(A)
    A.sort(key=lambda x: x[0])
    nextRange = [None] * n

    for i in range(n):
        nextRange[i] = binarySearch(A, i + 1, n - 1, A[i][1])

    bestIdx = None
    diff = float('inf')

    for i in range(n):
        idx = i
        cnt = 1

        if k == 1:
            if A[idx][1] - A[idx][0] < diff:
                diff = A[idx][1] - A[idx][0]
                bestIdx = i
        else:
            while idx < n and nextRange[idx] is not None:
                idx = nextRange[idx]
                cnt += 1
                if cnt == k:
                    if diff > A[idx][1] - A[i][0]:
                        diff = A[idx][1] - A[i][0]
                        bestIdx = i
                        break

    res = []
    cnt = 0

    if bestIdx is not None:
        while cnt < k:
            res.append(A[bestIdx])
            cnt += 1
            bestIdx = nextRange[bestIdx]

    return res, diff
