# mam tablice A rozmiaru n, która zawiera przedziały [a,b]
# przedziały [a,b] i [c,d] da sie skleic wtw gdy b == c
# mam rowniez wartosc x oraz y które stanowią poczatek i koniec przedziału
# znajdz wszystkie przedziały których sklejenie pozwala utworzyc przedział [x,y]

# O(nlogn)

def binarySearch(A, l, r, x):
    if l <= r:
        mid = l + (r - l) // 2
        if A[mid] == x:
            return mid
        elif x < A[mid]:
            return binarySearch(A, l, mid - 1, x)
        else:
            return binarySearch(A, mid + 1, r, x)
    return None


def dfs(G, s):
    n = len(G)
    visited = [False] * n

    def dfsVisit(u):
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                dfsVisit(v)

    dfsVisit(s)
    return visited


# odwracam wszystkie krawędzie
def reverseEdges(G):
    n = len(G)
    newG = [[] for _ in range(n)]

    for u in range(n):
        for v in G[u]:
            newG[v].append(u)
    return newG


def intuse(A, x, y):
    n = len(A)
    oryginalA = A.copy()
    A1 = A.copy()
    uniq1 = []
    uniq2 = []

    A.sort(key=lambda x: x[0])
    A1.sort(key=lambda x: x[1])

    # mam 2 tablice: jedną posortowaną po początkach a drugą po końcach
    # tworze 2 tablice elementow unikatowych:
    # do 1 zapisuje wszystkie wartosci początkowe bez powtorzen
    # do 2 zapisuje wszystkie wartosci koncowe bez powtorzen
    for i in range(n):
        if i == 0 or A[i][0] != A[i - 1][0]:
            uniq1.append(A[i][0])
        if i == 0 or A1[i][1] != A1[i - 1][1]:
            uniq2.append(A1[i][1])

    # z tablicy unikatów początkowych i końcowych tworze 1 tablice
    # w której zapisuje wszystkie wartosci z 1 i 2 tylko bez kopii
    uniq = []
    i, j = 0, 0
    while i < len(uniq1) and j < len(uniq2):
        if uniq1[i] == uniq2[j]:
            uniq.append(uniq1[i])
            i += 1
            j += 1
        elif uniq1[i] < uniq2[j]:
            uniq.append(uniq1[i])
            i += 1
        else:
            uniq.append(uniq2[j])
            j += 1

    while i < len(uniq1):
        uniq.append(uniq1[i])
        i += 1

    while j < len(uniq2):
        uniq.append(uniq2[j])
        j += 1

    # rozmiar grafu
    m = len(uniq)
    G = [[] for _ in range(m)]

    # dodaje krawędź w grafie między początkiem a końcem przedziału
    for i in range(n):
        u = binarySearch(uniq, 0, m - 1, A[i][0])
        v = binarySearch(uniq, 0, m - 1, A[i][1])
        G[u].append(v)

    start, end = binarySearch(uniq, 0, m - 1, x), binarySearch(uniq, 0, m - 1, y)

    if start is None or end is None:
        return []

    # dfs od poczatku przedziału
    visited1 = dfs(G, start)
    # odwracam krawędzie i puszczam dfs od konca przedziału
    G = reverseEdges(G)
    visited2 = dfs(G, end)

    A1 = []
    for i in range(m):
        if visited1[i] and visited2[i]:
            A1.append(uniq[i])

    res = []
    for i in range(n):
        if binarySearch(A1, 0, len(A1) - 1, oryginalA[i][0]) is not None \
                and binarySearch(A1, 0, len(A1) - 1, oryginalA[i][1]) is not None:
            res.append(i)

    return res


A = [[3, 4], [2, 5], [1, 3], [4, 6], [1, 4]]
x, y = 1, 6
print(intuse(A, x, y))