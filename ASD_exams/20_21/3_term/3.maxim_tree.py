# mam na wejsciu drzewo pełne binarne oraz tablice C z wartosciami
# te wartosci w C odpowiadają 'indeksom' w drzewie
# indeksy drzewa zaczynaja się od 1 i są w kolejnosci level-order tzn:
#    1
#  2   3
# 4  5 6  7 itd
# kazdemu indeksowi odpowiada jakas wartosc
# przejdz po wszystkich wartosciach z C i znajdz jaka najwieksza wartosci kryje sie
# pod jednym z zadanych indeksów

# 1) przechodzę po wartosciach z listy C
# 2) dla kazdej wartosci obliczam poziom na jakim znajduje się ona w drzewie binarnym
# 3) jesli wartosc jest parzysta tzn ze jest lewym dzieckiem, w przeciwnym wypadku - prawym,
# na bazie tej informacji przechodze drzewo po poziomach i zapamietuje sciezke
# 4) majac sciezke przechodze po drzewie i sprawdzam czy klucz na jaki trafie jest lepszy od ostatnio zapamiętanego

# zlożoność obliczeniowa: O(mlogn)
# złozoność pamięciowal: O(logn) - da się zrobić z pamięcią O(1)!

from math import log, ceil


def maxim(T, C):
    maxi = -float('inf')

    for el in C:

        level = ceil(log(el, 2))
        if log(el, 2) == ceil(log(el, 2)):
            level += 1

        path = []
        node = el
        while level > 1:
            if node % 2 == 0:
                path.append('l')
            else:
                path.append('r')
            node //= 2
            level -= 1

        path = path[::-1]

        root = T
        for move in path:
            if move == 'l':
                root = root.left
            else:
                root = root.right

        maxi = max(maxi, root.key)

    return maxi
