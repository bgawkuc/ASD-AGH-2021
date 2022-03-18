# Proszę zaimplementować funkcję:
# int SumBetween(int T[], int from, int to, int n);
# Zadaniem tej funkcji jest obliczyć sumę liczb z n elementowej tablicy T, które w posortowanej
# tablicy znajdywałyby się na pozycjach o indeksach od from do to (włącznie). Można przyjąć, że
# liczby w tablicy T są parami różne (ale nie można przyjmować żadnego innego rozkładu danych).
# Zaimplementowana funkcja powinna być możliwie jak najszybsza

def insertionSort(T, l, r):
    for i in range(l + 1, r + 1):
        j = i - 1
        el = T[i]
        while j >= l and T[j] > el:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = el
    return T


def getMedian(T, l, n):
    r = l + n - 1
    insertionSort(T, l, r)
    return l + (n - 1) // 2


def medianOfMedians(T, l, r):
    n = r - l + 1

    if n % 5 == 0:
        cnt_med = n // 5
    else:
        cnt_med = n // 5 + 1

    i = l

    while i * 5 + 4 < n:
        m = getMedian(T, i * 5, 5)
        T[m], T[i] = T[i], T[m]
        i += 1

    if i * 5 < n:
        m = getMedian(T, i * 5, n % 5)
        T[m], T[i] = T[i], T[m]

    if cnt_med == 1:
        return 0
    elif cnt_med < 6:
        return getMedian(T, l, cnt_med)
    else:
        return medianOfMedians(T, l, l + cnt_med - 1)


def partition(T, l, r, pivot):
    for i in range(l, r):
        if T[i] == pivot:
            T[i], T[r] = T[r], T[i]
            break
    pivot = T[r]
    i = l - 1

    for j in range(l, r):
        if T[j] < pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    i += 1
    T[i], T[r] = T[r], T[i]
    return i


def quickSelect(T, l, r, k):
    m = medianOfMedians(T, l, r)
    q = partition(T, l, r, T[m])

    if q - l == k:
        return q
    elif k < q - l:
        return quickSelect(T, l, q - 1, k)
    else:
        return quickSelect(T, q + 1, r, k - q - 1 + l)


def sum_beetween(T, start, end):
    s = quickSelect(T, 0, len(T) - 1, start)
    e = quickSelect(T, s, len(T) - 1, end - s)
    sum_ = 0
    for i in range(s, e + 1):
        sum_ += T[i]
    return sum_


t = [7, 1, 0, 4, 3, 6, 5, 2]
t1 = [90, 2, 12, 3, 0, 1, 7, 10, 19, 12, 21, 67, 31, 17]
print(sum_beetween(t1, 8, 10))
