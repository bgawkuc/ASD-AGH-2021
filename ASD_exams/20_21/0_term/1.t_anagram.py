# Rozważmy słowa x[0]x[1] · · · x[n − 1] oraz y[0]y[1] · · · y[n − 1] składające się z małych liter alfabetu łacińskiego.
# Takie dwa słowa są t-anagramem (dla t ∈ {0, . . . , n − 1}), jeśli każdej literze
# pierwszego słowa można przypisać taką samą literę drugiego, znajdującą się na pozycji różniącej
# się o najwyżej t, tak że każda litera drugiego słowa jest przypisana dokładnie jednej literze słowa
# pierwszego.
# Proszę zaimplementować funkcję:
# def tanagram(x, y, t):
# ...
# która sprawdza czy słowa x i y są t-anagramami i zwraca True jeśli tak a False w przeciwnym razie.
# Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową
# i pamięciową użytego algorytmu.

from collections import deque


def tAnagram(x, y, t):
    n = len(x)
    cnt = [0] * 26  # zlicza ilosc wystąpień danej litery
    idx = [deque() for _ in range(26)]

    for i in range(n):
        cnt[ord(x[i]) - ord('a')] += 1
        idx[ord(x[i]) - ord('a')].append(i)

    for i in range(n):
        cnt[ord(y[i]) - ord('a')] -= 1
        if cnt[ord(y[i]) - ord('a')] == -1:
            return False

        id = idx[ord(y[i]) - ord('a')].popleft()
        if abs(id - i) > t:
            return False

    return True


x = 'kotomysz'
y = 'tokmysoz'

print(tAnagram(x, y, 3))
