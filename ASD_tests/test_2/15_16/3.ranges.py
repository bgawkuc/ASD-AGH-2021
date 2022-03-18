# Zbiór przedziałów {[a1, b1], ..., [an, bn]}, każdy przedział należy do [0, 1]. Opisać algorytm który
# # sprawdzi czy jest możliwy taki wybór przedziałów, aby cały przedział [0, 1] zawierał się w
# # wybranych odcinkach. Przedział ma składać się z jak najmniejszej ilości odcinków.

def ranges(A):
    n = len(A)

    for i in range(n):
        A[i] = [A[i][0], A[i][1], i]

    nextRange = [None] * n
    A.sort(key=lambda x: x[0])

    for i in range(n):
        s, e, _ = A[i]
        for j in range(i + 1, n):
            if e >= A[j][0] and A[i][1] < 1 and (nextRange[i] is None or A[j][1] > A[nextRange[i]][1]):
                nextRange[i] = j

    i = 0
    bestIdx = None
    cnt = float('inf')

    while A[i][0] == 0.0:
        idx = i
        currCnt = 1

        while nextRange[idx] is not None:
            idx = nextRange[idx]
            currCnt += 1
            if A[idx][1] == 1:
                if cnt > currCnt:
                    cnt = currCnt
                    bestIdx = i
                break
        i += 1

    if bestIdx is None:
        return None

    res = []
    while bestIdx is not None and A[bestIdx][1] <= 1:
        res.append(A[bestIdx][2])
        bestIdx = nextRange[bestIdx]

    return res


t = [[0.0, 0.3], [0.0, 0.1], [0.15, 0.3], [0.4, 1], [0.3, 0.4], [0.2, 0.6], [0.3, 0.7], [0.6, 1], [0.7, 0.8], [0.75, 1]]
print(ranges(t))
