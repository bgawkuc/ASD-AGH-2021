# Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
# jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
# że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
# cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
# liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
# 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
# Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
# pretty_sort(T), która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
# powinien być możliwie jak najszybszy.


def reverse_tab(T):
    n = len(T)
    for i in range(n // 2):
        T[i], T[n - i - 1] = T[n - i - 1], T[i]
    return T


def cnt_digits(T):
    n = len(T)
    # idx 0-liczba, idx 1-ile jednokr,idx 2-ile wielokr
    cnt = [[0, 0, 0] for _ in range(n)]

    for i in range(n):
        cnt[i][0] = T[i]
        num = T[i]
        dig = [0] * 10

        while num > 0:
            last = num % 10
            dig[last] += 1
            num //= 10

        one, more = 0, 0

        for j in dig:
            if j == 1:
                one += 1
            elif j > 1:
                more += 1

        cnt[i][1] = one
        cnt[i][2] = more
    return cnt


def counting_sort(T, i):
    n = len(T)
    res = [None] * n
    new = cnt_digits(T)
    count = [0] * 11

    for j in range(n):
        count[new[j][i]] += 1

    for j in range(1, 11):
        count[j] += count[j - 1]

    for j in range(n - 1, -1, -1):
        count[new[j][i]] -= 1
        res[count[new[j][i]]] = T[j]

    for j in range(n):
        T[j] = res[j]

    return T


def pretty_sort(T):
    for i in range(2, 0, -1):
        counting_sort(T, i)
        T = reverse_tab(T)
    return T


t = [111, 117, 127, 1341, 12, 1819, 1023, 19876522]
print(pretty_sort(t))
