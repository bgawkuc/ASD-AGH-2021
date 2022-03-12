# Czołg jedzie z punktu 0 do punktu A. Spalanie czołgu to dokładnie jeden litr paliwa na jeden kilometr trasy.
# W baku mieści się dokładnie L litrów paliwa. Trasa z 0 do A to prosta, na której znajdują się stacje benzynowe.
# Wyznaczamy stacje na których tankujemy tak, żeby łączna liczba tankowań była minimalna. Gdy czołg zatrzymuje się
# na stacji to tankuje na niej do pełna.


# S-tablica indeksów, w których są stacje (posortowana)
def tank(A, L, S):
    currLocation = 0  # obecna lokalizacja
    cnt = 0  # ilosc odwiedzonych stacji
    lastStation = -1  # indeks stacji odwiedzonej ostatnio, na poczatku żadna to -1

    while True:

        if A - currLocation <= L:
            return cnt

        longestDist = currLocation + L  # jak najdalej moge dojechac na pelnym baku
        idx = lastStation  # indeks ostatnio odwiedzonej stacji

        while idx + 1 < len(S) and S[idx + 1] <= longestDist:
            idx += 1

        if (idx == lastStation):
            return None

        lastStation = idx
        cnt += 1
        currLocation = S[idx]