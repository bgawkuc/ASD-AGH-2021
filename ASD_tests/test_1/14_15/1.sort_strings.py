# Napisać funkcję: void sortString(string A[]); Funkcja sortuje tablicę n stringów różnej
# długości. Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.


def countingSortByLength(T):
    n = len(T)
    new = [None] * n
    maxi = len(max(T, key=len))
    cnt = [0] * (maxi + 1)

    for i in range(n):
        cnt[len(T[i])] += 1

    for i in range(1, maxi + 1):
        cnt[i] += cnt[i - 1]

    for i in range(n):
        cnt[len(T[i])] -= 1
        new[cnt[len(T[i])]] = T[i]

    for i in range(n):
        T[i] = new[i]

    return T


def countingSortByLetter1(T, let):
    n = len(T)
    new = [None] * n
    cnt = [0] * 26

    for i in range(n):
        cnt[ord(T[i][let]) - ord('a')] += 1

    for i in range(1, 26):
        cnt[i] += cnt[i - 1]

    for i in range(n - 1, -1, -1):
        cnt[ord(T[i][let]) - ord('a')] -= 1
        new[cnt[ord(T[i][let]) - ord('a')]] = T[i]

    for i in range(n):
        T[i] = new[i]

    return T


def sortStrings(T):
    n = len(T)
    countingSortByLength(T)
    maxSize = len(T[n - 1])

    for i in range(maxSize - 1, -1, -1):
        while n > 0 and len(T[n - 1]) > i:
            n -= 1
        T[n:] = countingSortByLetter1(T[n:], i)
    return T


t = ['kot', 'ma', 'ale', 'ala', 'kota', 'ma']
print(sortStrings(t))
