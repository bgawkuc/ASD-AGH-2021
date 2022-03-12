# Proszę zaproponować algorytm, który mając dane dwa słowa A i B o długości n, każde nad
# alfabetem długości k, sprawdza czy A i B są swoimi anagramami.

#zlozonosc O(n+k)

from random import randint

#dla alfabetu rozmiaru 2^16
def alloc(n):
    return [randint(0, 1000000000) for _ in range(n)]

def annagrams(w1,w2):
    if len(w1) != len(w2):
        return False

    counters = alloc(2 ** 16)

    n = len(w1)
    for i in range(n):
        counters[ord(w1[i])] = 0

    for i in range(n):
        counters[ord(w1[i])] += 1
        counters[ord(w2[i])] -= 1

    for i in range(n):
        if counters[ord(w1[i])] != 0:
            return False

    return True