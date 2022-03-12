# Czołg jedzie z punktu 0 do punktu A. Spalanie czołgu to dokładnie jeden litr paliwa na jeden kilometr trasy.
# W baku mieści się dokładnie L litrów paliwa. Trasa z 0 do A to prosta, na której znajdują się stacje benzynowe.
# Wyznaczamy stacje tak, żeby koszt przejazdu był minimalny (w tym wypadku każda stacja ma dodatkowo cenę za litr paliwa).
# Na każdej stacji możemy tankować dowolną ilość paliwa.

# S,P-tablice z indeksami stacji i cenami w nich
def tank(S, P, L, end):
    station = [False] * (end + 1)
    price = [None] * (end + 1)

    for idx in range(len(S)):
        station[S[idx]] = True
        price[S[idx]] = P[idx]

    cost = 0  # koszt podrozy
    idx = 0  # obecny indeks
    currGas = L  # obecna ilosc paliwa

    while True:
        if idx + currGas >= end:
            return cost

        # szukam najblizszej stacji i na nią jadę
        new = None
        for i in range(idx + 1, idx + L + 1):
            if i <= end and station[i]:
                new = i
                currGas -= (i - idx)
                break

        if new is None:
            return False
        else:
            idx = new

        # szukam stacji w zasięgu baku z tanszych paliwem
        new = None
        for i in range(idx + 1, idx + L + 1):
            if i <= end and station[i] and price[i] < price[idx]:
                new = i
                break

        # gdy nie ma w zasiegu stacji idx stacji z tanszym paliwem
        if new is None:

            if idx + L >= end:
                missing = currGas - (end - idx)
                if missing < 0:
                    cost += (abs(missing) * price[idx])
                    currGas += abs(missing)
                return cost

            else:
                cost += ((L - currGas) * price[idx])
                currGas = L

        # gdy w zasięgu jest tansza stacja to tankuje tyle by dostac sie na nią
        else:
            missing = currGas - (new - idx)
            if missing < 0:
                cost += (abs(missing) * price[idx])
                currGas += abs(missing)
