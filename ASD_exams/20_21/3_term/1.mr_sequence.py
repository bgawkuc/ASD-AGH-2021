# dostaje na wejsciu tablice liczb
# mam 3 rodzaje ciagów:
# 1)scisle rosnacy
# 2)scisle malejący
# 3)bitoniczny - najpierw maleje potem rośnie
# znajdz najdłuższy podciag w tablicy typu 1,2 lub 3 i go wypisz


# zlożoność obliczeniowa O(n^2) - jak się lepiej zaimlpelementuje lis(lbs) to byłoby O(nlogn)
# złożoność pamięciowa O(n)

def mr(X):
    n = len(X)

    # dpLis[i] - dlg lis, który zaczyna się na indeksie i-tym
    dpLis = [1] * n
    # zapamietuje 'drogę' lis
    pLis = [None] * n

    # dpLds[i] - dlg lds, który konczy się na indeksie i-tym
    dpLds = [1] * n
    # zapamiętuje 'drogę' lds
    pLds = [None] * n

    # dpLbs[i] - dlg lbs, który na indeksie i-tym przestaje maleć a zaczyna rosnąć
    dpLbs = [1] * n

    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if X[i] < X[j] and dpLis[j] + 1 > dpLis[i]:
                dpLis[i] = dpLis[j] + 1
                pLis[i] = j

    for i in range(n):
        for j in range(i):
            if X[i] < X[j] and dpLds[j] + 1 > dpLds[i]:
                dpLds[i] = dpLds[j] + 1
                pLds[i] = j

    for i in range(n):
        dpLbs[i] = dpLds[i] + dpLis[i] - 1

    maxi = -float('inf')
    bestIdx = None
    type = None

    if max(dpLis) > maxi:
        maxi = max(dpLis)
        type = 'lis'

        for i in range(n):
            if dpLis[i] == maxi:
                bestIdx = i
                break

    if max(dpLds) > maxi:
        maxi = max(dpLds)
        type = 'lds'

        for i in range(n):
            if dpLds[i] == maxi:
                bestIdx = i
                break

    if max(dpLbs) > maxi:
        maxi = max(dpLbs)
        type = 'lbs'

        for i in range(n):
            if dpLbs[i] == maxi:
                bestIdx = i
                break

    res = []

    # odtwarzam malejący
    if type == 'lds' or type == 'lbs':
        i = bestIdx
        while i is not None:
            res.append(X[i])
            i = pLds[i]

        res = res[::-1]

    # odtwarzam rosnący
    if type == 'lis' or type == 'lbs':
        i = bestIdx
        if type == 'lbs':
            i = pLis[i]
        while i is not None:
            res.append(X[i])
            i = pLis[i]

    return res


A = [4, 10, 5, 1, 8, 2, 3, 4]
print(mr(A))
